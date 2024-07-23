# SE-Practice

```
  |-- be
        |-- model
        |-- view
            |-- translate       
            |-- correct
            |-- summary
            |-- ocr
        |-- ....
  |-- fe
```

# 通义千问api使用方法

在使用前将api_key填到be/utils/key.py中的对应位置

# 接口文档
body后有标注的上传文件，其它上传json

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

