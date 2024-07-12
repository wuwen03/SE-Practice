// pages/main/main.js
Page({
    /**
     * 页面的初始数据
     */
    data: {
      // 这里可以初始化一些数据
      message: 'Hello, this is the main page!'
    },
  
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
      // 页面加载时调用此函数，options 是页面传递的参数对象
      console.log('Page loaded with options:', options);
    },
  
    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {
      // 页面初次渲染完成时调用此函数
      console.log('Page ready');
    },
  
    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {
      // 页面显示时调用此函数
      console.log('Page shown');
    },
  
    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {
      // 页面隐藏时调用此函数
      console.log('Page hidden');
    },
  
    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {
      // 页面卸载时调用此函数
      console.log('Page unloaded');
    },
  
    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {
      // 用户下拉刷新页面时调用此函数
      console.log('Pulling down to refresh');
      // 在这里处理数据刷新逻辑
    },
  
    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {
      // 用户上拉触底时调用此函数
      console.log('Reached bottom');
      // 在这里处理加载更多数据的逻辑
    },
  
    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {
      return {
        title: '分享标题',
        path: 'pages/main/main'
      };
    },
    handleButtonClickIss: function(e) {
        // 处理按钮点击事件
        console.log('Button iss clicked');
        wx.navigateTo({
            url: '/pages/iss/iss'
          });
      },
    
    // 自定义方法
    customMethod: function() {
      console.log('Custom method called');
    }
  })