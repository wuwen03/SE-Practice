function success(tip) {
    wx.showToast({
        title: tip,
        icon: 'success',
        duration: 1000
    });
}

function loading(tip) {
    wx.showLoading({
        title: tip,
        mask: true
    });
}

function noloading() {
    wx.hideLoading({});
}

function hideToust() {
    wx.hideToast({});
}

function error(code) {
    wx.showToast({
        title: "error:" + code,
        icon: 'error',
        duration: 1000
    });
}


/**
 * 
 * 模态框 
 */
function prompt(tip) {
    wx.showModal({
        title: '提示',
        content: tip,
        showCancel: false
    })
}

module.exports = {
    success, loading, noloading, error, prompt, hideToust
}