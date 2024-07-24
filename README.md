# 需求文档
# 系统概述

## 产品概述
针对校内留学生日常生活、学习、交流提供帮助的微信小程序

## 用户特征
校内留学生，以及留学生的老师  

## 设计和实现约束
根据用户的不同需求提供不同语言支持，界面简单便于不熟悉国产软件的用户使用

# 功能需求描述
## translate部分
根据用户选择使用的语言，将输入文本转化为相应的语言
## correct部分
给用户输入的文本做一个智能批改，也提供文件上传
## summary部分
给用户输入的文本做一个智能摘要，也提供文件上传
## ocr部分
接受用户的一张图片，然后可以提取图片中文字，然后可以选择翻译为用户使用的语言

# 界面
进入主界面后，左上角用户选择使用的语言，然后通过四个按钮进入不同功能。  

# 接口定义

## translate

#### URL：
POST http://$address$/translate/

#### Request

Body:
```
{
    "src_language":"$src_language$",
    "dst_language":"$dst_language$",
    "content":"$content$"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
src_language | string | 输入语言 | N
dst_language | string | 输出语言 | N
content | string | 要翻译的内容 | N

#### Response

Status Code:


码 | 描述
--- | ---
200 | 翻译成功
5XX | 失败

Body:
```
{
    "result":"$result$"
    "message":"$error message$"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
result | string | 翻译结果内容 | N
message | string | 返回错误消息，成功时为"ok" | N


## ocr

#### URL：
POST http://$address$/ocr/upload

#### Request

Body(files):
```
{
    "file":"$pic_file$"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
pic_file | file | 图片文件 | N

#### Response

Status Code:


码 | 描述
--- | ---
200 | 文字识别成功
5XX | 失败

Body:
```
{
    "result":"$result$"
    "message":"$error message$"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
result | string | 识别结果内容文字 | N
message | string | 返回错误消息，成功时为"ok" | N


## correct

#### URL1：
POST http://$address$/correct/

#### Request1

Body:
```
{
    "content":"$content$"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
content | string | 要批改的内容 | N

#### URL2：
POST http://$address$/correct/upload

#### Request2

Body(files):
```
{
    "file":"$file$"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
file | file | .pdf .txt .docx文件 | N


#### Response

Status Code:


码 | 描述
--- | ---
200 | 批改成功
5XX | 失败

Body:
```
{
    "result":"$result$"
    "message":"$error message$"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
result | string | 批改结果内容 | N
message | string | 返回错误消息，成功时为"ok" | N



## summary

#### URL1：
POST http://$address$/summary/

#### Request1

Body:
```
{
    "content":"$content$"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
content | string | 要摘要的内容 | N

#### URL2：
POST http://$address$/summary/upload

#### Request2

Body(files):
```
{
    "file":"$file$"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
file | file | .pdf .txt .docx文件 | N

#### Response

Status Code:


码 | 描述
--- | ---
200 | 摘要成功
5XX | 失败

Body:
```
{
    "result":"$result$"
    "message":"$error message$"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
result | string | 摘要结果内容 | N
message | string | 返回错误消息，成功时为"ok" | N

# 进度与交付
第一周：规划与设计，学习开发所需技术，明确功能和分工   
第二周：部署服务器连通前后端，前端界面设计，后端框架搭建，连接大模型   
第三周：具体实现四大基础功能模块，编写测试用例并跑通，大模型对比与微调  
第四周：新增加图片上传、文件上传功能，bug修复




