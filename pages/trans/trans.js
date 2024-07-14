Page({
    data: {
      originalText: '',
      translatedText: '',
      errorMessage: ''
    },
    onInputChanged: function(e) {
      this.setData({ originalText: e.detail.value });
    },
    onTranslate: async function() {
      const { originalText } = this.data;
      if (originalText.trim() === '') return;
      console.log('originalText');
      try {
        const response = await wx.request({
          url: 'https://47.113.205.144:5000/ecs/translate',
          method: 'POST',
          data: { 
            "src_language":getApp().globalData.chosen_language,
            "dst_language":"CN",
            "content":originalText },
          header: {
            'content-type': 'application/json'
          }
        });
  
        if (response.statusCode === 200 && response.data && response.data.result) {
          this.setData({ translatedText: response.data.result });
        } else {
          this.setData({ errorMessage: response.data.message || '翻译失败，请重试。' });
        }
      } catch (error) {
        this.setData({ errorMessage: '网络请求失败，请检查网络连接。' });
        console.error('Translation failed:', error);
      }
    }
  });
//基于   {
//     "result": "$translated_text$",
//     "message": "$error_message$"
// }
//   data: { 
//     "src_language":"$src_language$",
//     "dst_language":"$dst_language$",
//     text: originalText },