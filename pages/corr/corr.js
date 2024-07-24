//const md5 = require('../../utils/md5.js');
const window = require('../../utils/window.js'); /*调用加载界面*/
//const dbf = require('../../utils/dbf.js');
//const app = getApp();

Page({
    input(e) {
        this.curText = e.detail.value;
    },
    
    setRes() {

        var rli = [];
        for (var i = 0; i < this.curRes.length; i++) 
        {
            rli[i] = { 'text': this.curRes[i].text, 'bg': this.curRes[i].tag == 0 ? "white" : "#00B26A" }
        }


        this.setData({
            resli: rli
        });

    },

    submmit() 
    {
        window.loading("纠错中");

        var then = this;
        /*
        console.log("进去了");
        console.log(then.curText);
        */
        wx.request({
            url: 'http://47.113.205.144:5000/correct/',
            data: {
                text: then.curText
            },
            header: { 'content-type': 'application/json' },
            method: 'POST',
            dataType: 'json',
            responseType: 'text',
            success: (res) => {
                /*
                console.log("出来了");
                console.log(res);
                */
                if (res.statusCode != 200) 
                {
                    window.error(res.statusCode);
                    return;
                }

                window.success("纠错成功");
                //console.log(res.data);
                then.curRes = res.data;
                //console.log(then.curRes);
                then.setRes();
                /*
                var d = new Date();
                var time = d.getFullYear() + "/" + d.getMonth() + "/" + d.getDate() + " " + d.getHours() + ":" + d.getMinutes();


                var his = {
                    time: time,
                    title: then.curText.substr(0, 8) + "...",
                    bef: then.curText,
                    aft: then.curRes
                };

                app.globalData.histqu.push(his);

                dbf.updateHis(app.globalData.openid, app.globalData.histqu, function (res) { });
                */
            },
            fail: () => {

            },
            complete: () => { }
        });
    },

});