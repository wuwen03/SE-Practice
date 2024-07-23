Page({
    data: {  
      src: '', // 初始为空字符串，或者你也可以设置一个默认的图片路径  
      result: 'Nothing',
      translated: 'Nothing'
    },
    handleButtonClickIss1: function(e) {
      // 处理按钮点击事件
      wx.showLoading({  
        title: 'translating...', // 提示的内容  
      });  
      setTimeout(() => {  
        // 异步操作完成  
        wx.hideLoading();  
        // 更新数据等操作  
      }, 2000); // 假设异步操作耗时2秒  
      let that = this
      wx.request({  
        url: 'http://47.113.205.144:5000/translate/',
        method: 'POST',
        data: { 
          "src_language": getApp().globalData.chosen_language,
          "dst_language":"英语",
          "content":that.data.result
        },
        success: function (response) {
          that.setData({
            translated: response.data.result
          })
          console.log('发送成功', response.data);   
        },  
        fail: function (error) {  
          console.error('发送失败', error);   
        }  
      });  
    },
    sendPhotoToBackend() {   
      let that = this 
          wx.chooseMedia({
            count: 1,
            mediaType: 'image',
            sourceType: ['album', 'camera'],
            camera: 'back',
            success(res) {
              wx.showLoading({  
                title: '', // 提示的内容  
              });  
              setTimeout(() => {  
                // 异步操作完成  
                wx.hideLoading();  
                // 更新数据等操作  
              }, 2000); // 假设异步操作耗时2秒  
              that.setData({
                src : res.tempFiles[0].tempFilePath
              })
              wx.uploadFile({
                url: 'http://47.113.205.144:5000/ocr/upload',
                filePath: that.data.src,
                name: 'file',
                success: function(response) {
                  const temp = JSON.parse(response.data)
                  that.setData({
                    result: temp['result']
                  })
                  console.log('发送成功', response.data);
                }
              })
            }
          })
          console.log("fghfg")
        },  
})