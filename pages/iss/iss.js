Page({
    data: {
      array: ['China','America', 'Brazil', 'Japan'],
      objectArray: [
        {
          id: 0,
          name: '中国',
          pic:'https://flagcdn.com/w2560/cn.png',
          language:'CN'
        },
        {
          id: 1,
          name: '美国',
          pic:'https://flagcdn.com/w2560/us.png',
          language:'EN'
        },
        {
          id: 2,
          name: '巴西',
          pic:'https://flagcdn.com/w2560/br.png',
          language:'PU'
        },
        {
          id: 3,
          name: '日本',
          pic:'https://flagcdn.com/w2560/jp.png',
          language:'JP'
        }
      ],
      index: 0
      
    },
    bindPickerChange: function(e) {
      getApp().globalData.chosen_language=this.data.objectArray[e.detail.value].language;
      console.log('picker发送选择改变，携带值为', e.detail.value,'语言为',getApp().globalData.chosen_language)
      this.setData({
        index: e.detail.value
      })
      
    },
    handleButtonClickTRANS: function(e) {
        // 处理按钮点击事件
        console.log('Button translat clicked');
        wx.navigateTo({
            url: '/pages/trans/trans'
          });
      },
  })