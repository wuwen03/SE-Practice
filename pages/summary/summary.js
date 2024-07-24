Page({
  handleButtonClickSUM: function(e) {
    // 处理按钮点击事件
    console.log('Button summary clicked');
  },
  data:{
    summaryOutput:'',
    translatedOutput:''
  },
  chooseFile: function () {
    wx.chooseMessageFile({
      count: 1,
      type: 'file',
      success: res => {
        const tempFilePath = res.tempFiles[0].path;
        const fileType = tempFilePath.split('.').pop().toLowerCase();

        if (fileType === 'pdf' || fileType === 'doc' || fileType === 'docx' || fileType === 'txt') {
          this.readFile(tempFilePath, fileType);
        } else {
          wx.showToast({
            title: '不支持的文件类型',
            icon: 'none'
          });
        }
      },
      fail: err => {
        console.error(err);
      }
    });
  },

  readFile: async function (filePath, fileType) {
    wx.showLoading({
      title: '正在处理文件',
    });
    try{const formData = new FormData();
    formData.append('file',fs.createRoadStream(filePath));

    const summaryResponse = await axios.post('http://47.113.205.144:5000/summary/upload',formData,{headers: formData.getHeaders()
    });
    if(summaryResponse.status !== 200){
      throw new Error('Summarization failed with status ${summaryResponse.status}');
    }
    const{result:summary} = summaryResponse.data;
    const translateResponse = await axios.post('http://47.113.205.144:5000/translate/',{
      "src_language":getApp().globalData.chosen_language,
      "dst_language":"CN",
      "content":summary
    });
    if(translateResponse.status !== 200){
      throw new Error('Translation failed with status ${translateResponse.status}');
    }
    const translatedSummary = translateResponse.data.result;
    console.log('Translated Summary:',translatedSummary);
    return translatedSummary;
  }catch (error){
    console.error('Error:',error.message);
    throw error;
  }
    //wx.getFileSystemManager().readFile({
      //filePath: filePath,
      //encoding: 'utf-8',
      //success: res => {
        //const content = res.data;
        //let extractedText;

        //if (fileType === 'pdf') {
          //extractedText = this.extractPdfText(content);
        //} else if (fileType === 'doc' || fileType === 'docx') {
          //extractedText = this.extractDocxText(content);
        //} else if (fileType === 'txt') {
          //extractedText = fileContent;
        //}

        //this.setData({
          //summaryOutput: extractedText
        //});

        // 调用翻译函数，这里假设翻译函数为 translateText
        //const translatedText = this.translateText(extractedText);
        //this.setData({
          //translatedOutput: translatedText
        //});

        //wx.hideLoading();
      //},
      //fail: err => {
        //console.error(err);
        //wx.showToast({
          //title: '读取文件失败',
          //icon: 'none'
        //});
        //wx.hideLoading();
      //}
    //});
  },
})