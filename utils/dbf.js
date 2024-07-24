const md5 = require('../utils/md5');
wx.cloud.init({
    env: 'test-h8qbc'
});
const db = wx.cloud.database();

function isLogin(openid) {

}

function init(openid, userInfo, callback) {
    db.collection('Users').add({
        data: {
            uid: md5.hex_md5(openid),
            userInfo: userInfo,
            histqu: []
        },
        success: res => {
            callback(res);
        },
        fail: console.error
    });
}

function updateHis(openid, histqu, callback) {
    db.collection("Users").where({
        _openid: openid
    }).update({
        data: {
            histqu: histqu
        },
        success: res => {
            callback(res);
        },
        fail: console.error
    });
}



module.exports = {
    isLogin, init, updateHis
}