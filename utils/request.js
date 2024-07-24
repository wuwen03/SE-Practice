const window = require('./window');
const md5 = require('./md5.js');
const app = getApp();




/**
* @function 文件识别
* @description 先将文件上传至云存储，后请求文件识别接口
* @param url String 临时路径或本地路径
* @param type String 发送请求的类型/路由，内容应该是 ['text', 'image_write', 'image_print', 'audio']中之一
* @param ext String 本次上传文件的拓展名
* @param callback function completed类型的回调函数
* @return void
* @author wzq 2021/04/21 
* @example
*/
function readFile(url, type, ext, callback) {

    window.loading("识别中");

    wx.cloud.uploadFile({
        cloudPath: 'textCorr/' + md5.hex_md5(new Date().getTime() + app.globalData.openid) + '.' + ext, // 上传至云端的路径
        filePath: url, //本地路径
        success: res => {
            // 返回文件 ID

            wx.cloud.getTempFileURL({
                fileList: [res.fileID],
                success: res => {
                    var src = res.fileList[0].tempFileURL;
                    console.log("url: ", src);
                    wx.request({
                        url: 'http://42.192.50.88:5000/readfile',
                        data: {
                            url: src,
                            type: type
                        },
                        header: { 'content-type': 'application/json' },
                        method: 'GET',
                        dataType: 'json',
                        responseType: 'text',
                        success: (res) => {

                            console.log(res.data);

                            if (res.statusCode == 404) {
                                window.noloading();
                                window.prompt("维护中");
                                callback(res);
                                return;
                            }

                            if (res.statusCode >= 300) {
                                window.noloading();
                                window.prompt("网络错误");
                                callback(res);
                                return;
                            }
                            if (res.data.code != 2000) {
                                window.error(res.data.code);
                                // window.prompt("网络不可用");
                                callback(res);
                                return;
                            }

                            window.success("识别成功");
                            // window.error(404);


                            app.globalData.text = res.data.data.result;


                            callback(res);


                        },
                        fail: () => {
                            window.error("网络错误");
                        },
                        complete: () => { }
                    });
                },
                fail: console.error
            });
        },
        fail: console.error
    });
}

/**
* @function 上传文件
* @description 上传文件到云存储，成功后在回调函数中调用request中的文件识别函数
* @param acFileType Array<String> 可接受的文件类型，内容是拓展名
* @param type String 发送请求的类型/路由，内容应该是 ['text', 'image_write', 'image_print', 'audio']中之一
* @param callback function completed类型的回调函数
* @return String 临时文件地址或null
* @author wzq 2021/04/21 
* @example
*/
function upload(acFileType, callback) {

    wx.chooseMessageFile({
        count: 1,
        type: 'file',
        extension: acFileType,
        success(res) {

            var ac = false;
            var ftype = res.tempFiles[0].name.fileType();
            for (var i = 0; i < acFileType.length; i++) {
                if (ftype == acFileType[i].toLowerCase() || ftype == acFileType[i].toUpperCase()) {
                    ac = true;
                    break;
                }
            }

            if (!ac) {
                window.prompt("文件格式非法");
                return null;
            }

            if (res.tempFiles[0].size >= 1024 * 1024 * 10) {
                window.prompt("文件大小不能超过10Mb");
                return null;
            }

            callback({ "tempFilePath": res.tempFiles[0].path, "ext": res.tempFiles[0].path.fileType() });

        },
        fail: console.error
    });
}


module.exports = {
    readFile, upload
}