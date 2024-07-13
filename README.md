# SE-Practice

```
  |-- be
        |-- model
        |-- view
            |-- translate       
            |-- correct
            |-- summary
            |-- ocr
            |-- user(login register)
        |-- ....
  |-- fe
```

## 通义千问api使用方法

在使用前将api_key填到be/utils/api.py中的对应位置，然后在使用时候调用call_with_messages即可。参数是输入，返回值就是通义千问的输出。不过现在只支持文字的输入

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
POST http://$address$/ocr/

#### Request

Body:
```
{
    "picture":"$picture$"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
picture | string | 编码后的图片 | N

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

#### URL：
POST http://$address$/correct/

#### Request

Body:
```
{
    "content":"$content$"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
content | string | 要批改的内容 | N

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

#### URL：
POST http://$address$/summary/

#### Request

Body:
```
{
    "content":"$content$"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
content | string | 要摘要的内容 | N

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


## login

#### URL：
POST http://$address$/user/login

#### Request

Body:
```
{

}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---



#### Response

Status Code:


码 | 描述
--- | ---
200 | 登录成功
5XX | 失败

Body:
```
{
    "language":"$language$"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
language | string | 用户语言 | N
message | string | 返回错误消息，成功时为"ok" | N


## register

#### URL：
POST http://$address$/user/register

#### Request

Body:
```
{
    "language":"$language$"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
language | string | 用户选择的使用语言 | N

#### Response

Status Code:


码 | 描述
--- | ---
200 | 注册成功
5XX | 失败

Body:
```
{

}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N