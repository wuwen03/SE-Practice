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

## translate

#### URL��
POST http://$address$/translate

#### Request

Body:
```
{
    "src_language":"$src_language$",
    "dst_language":"$dst_language$",
    "content":"$content$"
}
```

������ | ���� | ���� | �Ƿ��Ϊ��
---|---|---|---
src_language | string | �������� | N
dst_language | string | ������� | N
content | string | Ҫ��������� | N

#### Response

Status Code:


�� | ����
--- | ---
200 | ����ɹ�
5XX | ʧ��

Body:
```
{
    "result":"$result$"
    "message":"$error message$"
}
```
������ | ���� | ���� | �Ƿ��Ϊ��
---|---|---|---
result | string | ���������� | N
message | string | ���ش�����Ϣ���ɹ�ʱΪ"ok" | N


## ocr

#### URL��
POST http://$address$/ocr

#### Request

Body:
```
{
    "picture":"$picture$"
}
```

������ | ���� | ���� | �Ƿ��Ϊ��
---|---|---|---
picture | string | ������ͼƬ | N

#### Response

Status Code:


�� | ����
--- | ---
200 | ����ʶ��ɹ�
5XX | ʧ��

Body:
```
{
    "result":"$result$"
    "message":"$error message$"
}
```
������ | ���� | ���� | �Ƿ��Ϊ��
---|---|---|---
result | string | ʶ������������ | N
message | string | ���ش�����Ϣ���ɹ�ʱΪ"ok" | N


## correct

#### URL��
POST http://$address$/correct

#### Request

Body:
```
{
    "content":"$content$"
}
```

������ | ���� | ���� | �Ƿ��Ϊ��
---|---|---|---
content | string | Ҫ���ĵ����� | N

#### Response

Status Code:


�� | ����
--- | ---
200 | ���ĳɹ�
5XX | ʧ��

Body:
```
{
    "result":"$result$"
    "message":"$error message$"
}
```
������ | ���� | ���� | �Ƿ��Ϊ��
---|---|---|---
result | string | ���Ľ������ | N
message | string | ���ش�����Ϣ���ɹ�ʱΪ"ok" | N



## summary

#### URL��
POST http://$address$/summary

#### Request

Body:
```
{
    "content":"$content$"
}
```

������ | ���� | ���� | �Ƿ��Ϊ��
---|---|---|---
content | string | ҪժҪ������ | N

#### Response

Status Code:


�� | ����
--- | ---
200 | ժҪ�ɹ�
5XX | ʧ��

Body:
```
{
    "result":"$result$"
    "message":"$error message$"
}
```
������ | ���� | ���� | �Ƿ��Ϊ��
---|---|---|---
result | string | ժҪ������� | N
message | string | ���ش�����Ϣ���ɹ�ʱΪ"ok" | N


## login

#### URL��
POST http://$address$/user/login

#### Request

Body:
```
{

}
```

������ | ���� | ���� | �Ƿ��Ϊ��
---|---|---|---



#### Response

Status Code:


�� | ����
--- | ---
200 | ��¼�ɹ�
5XX | ʧ��

Body:
```
{
    "language":"$language$"
}
```
������ | ���� | ���� | �Ƿ��Ϊ��
---|---|---|---
language | string | �û����� | N
message | string | ���ش�����Ϣ���ɹ�ʱΪ"ok" | N


## register

#### URL��
POST http://$address$/user/register

#### Request

Body:
```
{
    "language":"$language$"
}
```

������ | ���� | ���� | �Ƿ��Ϊ��
---|---|---|---
language | string | �û�ѡ���ʹ������ | N

#### Response

Status Code:


�� | ����
--- | ---
200 | ע��ɹ�
5XX | ʧ��

Body:
```
{

}
```
������ | ���� | ���� | �Ƿ��Ϊ��
---|---|---|---
message | string | ���ش�����Ϣ���ɹ�ʱΪ"ok" | N