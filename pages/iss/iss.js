Page({
    data: {
      array: ['China','America', 'Brazil', 'Japan'],
      objectArray: [
        {
          id: 0,
          name: '中国',
          pic:'https://flagcdn.com/w2560/cn.png'
        },
        {
          id: 1,
          name: '美国',
          pic:'https://flagcdn.com/w2560/us.png'
          
        },
        {
          id: 2,
          name: '巴西',
          pic:'https://flagcdn.com/w2560/br.png'
        },
        {
          id: 3,
          name: '日本',
          pic:'https://flagcdn.com/w2560/jp.png'
        }
      ],
      index: 0,
      
    },
    bindPickerChange: function(e) {
      console.log('picker发送选择改变，携带值为', e.detail.value)
      this.setData({
        index: e.detail.value
      })
    },
  })