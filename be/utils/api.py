import dashscope
from dashscope import Generation
from http import HTTPStatus
import random
from be.utils.logger import logger
from be.utils.key import QWEN_API_KEY
# from key import QWEN_API_KEY
# from logger import logger

APIKEY = QWEN_API_KEY
dashscope.api_key = QWEN_API_KEY

def call_with_messages(content:str):
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': content}]
    response = Generation.call(model="qwen-turbo",
                               messages=messages,
                               # 设置随机数种子seed，如果没有设置，则随机数种子默认为1234
                               seed=random.randint(1, 10000),
                               # 将输出设置为"message"格式
                               result_format='message')
    if response.status_code == HTTPStatus.OK:
        logger.info(response)
    else:
        logger.info('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
    return response.output.choices[0].message.content


from openai import OpenAI
import os
import base64
import mimetypes

def handle_image(img_path):
    image_path = img_path
    mime_type, _ = mimetypes.guess_type(image_path)    # 校验MIME类型为支持的图片格式    
    if mime_type and mime_type.startswith('image'):        
        with open(image_path, 'rb') as image_file:            # 将图片内容转换为Base64字符串            
            encoded_image = base64.b64encode(image_file.read())            
            encoded_image_str = encoded_image.decode('utf-8')            # 创建数据前缀            
            data_uri_prefix = f'data:{mime_type};base64,'            # 拼接前缀和Base64编码的图像数据            
            encoded_image_str = data_uri_prefix + encoded_image_str
        return "ok", encoded_image_str
    else:
        return "invalid type", bytes()

#图片用base64的格式提交
def call_with_image(encoded_image_str, content) -> str:    
    client = OpenAI(        
        api_key=APIKEY,        
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",    
    )      
    # isvalid, encoded_image_str = handle_image(img_path)  
    # if isvalid != "ok":
    #     return ""                     
    completion = client.chat.completions.create(                
            model="qwen-vl-plus",                
            messages=[                    
                {                        
                    "role": "user",                        
                    "content": [                            
                                    {                                
                                        "type": "text",                                
                                        "text": content                            
                                    },                            
                                    {                                
                                        "type": "image_url",                                
                                        "image_url": {                                    
                                            "url": encoded_image_str                                
                                        }                            
                                    }                        
                                ]                    
                }                
            ],                
            top_p=0.8,                
            # stream=False,                
            # stream_options={"include_usage": True}            
        )            
        # for chunk in completion:                
        #     print(chunk.model_dump_json())    
        # else:        
        #     print("MIME type unsupported or not found.")
    res = completion.choices[0].message.content
    # print(res)
    return res         

import requests
import json
def get_certificate(model:str = "qwen-vl-plus"):
    url = 'https://dashscope.aliyuncs.com/api/v1/uploads'
    header = {
        "Content-Type" : "application/json",
        "Authorization" : "Bearer " + APIKEY,
    }
    query = {
        "action" : "getPolicy",
        "model" : model
    }
    resp = requests.get(url=url,headers=header,params=query)
    print(resp.request.url)
    print(resp.request.headers)
    print(resp.request.body)
    print(resp.content)
    return json.loads(str(resp.content,"ascii"))
    


def upload_file(file_path:str,):
    name = file_path.split('/')[-1]
    cert = get_certificate()
    url = cert['data']['upload_host']
    header = {
        "Content-Type" : "multipart/form-data;boundary=9431149156168",
        "x-oss-object-acl" : cert['data']['x_oss_object_acl']
    }
    file = {
        "OSSAccessKeyId" : cert['data']['oss_access_key_id'],
        "policy" : cert['data']['policy'],
        "Signature" : cert['data']['signature'],
        "key" : cert['data']['upload_dir']+"/"+"name",
        "x-oss-object-acl" : cert['data']['x_oss_object_acl'],
        "x-oss-forbid-overwrite" : cert['data']['x_oss_forbid_overwrite'],
        "file" : open(file_path,'rb')
    }
    resp=requests.post(url=url,files=file)
    print(str(resp.request.url))
    print(str(resp.request.headers))
    print(str(resp.request.body))
    print(resp.content)
    # return "oss://"+cert['data']['upload_dir']+file_path
    return "oss://"+cert['data']['upload_dir']+"/"+"name"

def call_with_file(file_path):
    file_url = upload_file(file_path=file_path)
    print(file_url)
    url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation'
    header = {
        "Content-Type" : "application/json",
        "Authorization" : "Bearer " + APIKEY,
        "X-DashScope-OssResourceResolve" : "enable"
    }
    data = {
        "model" : "qwen-vl-plus",
        "input" : {
            "messages" : [
                {
                    "role" : "user",
                    "content" : [
                        {
                            "text":"判断作文好坏："
                        },
                        {
                            "image":file_url
                        }
                    ]
                }
            ]
        }
    }
    # print(str(json.dumps(data)))
    resp = requests.post(url=url,headers=header,json=data)
    # print(json.loads(str(resp.content,"ascii")))
    print(str(resp.request.body,"ascii"))
    print(json.loads(resp.content))


if __name__ == "__main__":   
    pass
    # upload_file('/root/se_practice/test/hello.txt')
    # call_with_file('/root/se_practice/test/作文.png')