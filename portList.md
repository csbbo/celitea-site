
####服务器首页文章返回
```
[
    {
        "article": "文章内容",
        "article_title": "文章标题",
        "id": 1,
        "time": "Fri, 10 Aug 2018 20:39:10 GMT",
        "user_id": 2
    },
    {
        "article": "文章内容",
        "article_title": "文章标题",
        "id": 2,
        "time": "Fri, 10 Aug 2018 20:40:14 GMT",
        "user_id": 2
    },
    {
        "article": "文章内容",
        "article_title": "文章标题",
        "id": 3,
        "time": "Fri, 10 Aug 2018 20:41:24 GMT",
        "user_id": 2
    }
]
```
-------------------------------
###注册
####客户端注册信息发送
```
{
    user:{
        userName:'',
        userPassword:'',
        userPhoneNumber:'',
        userIdentifyingCode:''
    }
}
```
####服务器注册状态返回
```
{
    registerStatus:'success'|| registerStatus:'fail'|| registerStatus :'wrongCode'
}
```
----------------------------
###登录
####客户端登陆信息发送
```
{
    user:{
        userPhoneNumber:'',
        userPassword:''
    }
}
```

####服务器登陆信息返回
```
{
    loginStatus:'success'|| loginStatus:'fail'
}
```

####服务器登陆状态返回
```
{
    userStatis:'true' || userStatis:'false',
    userName:''
}
```
------------
###注销
####客户端注销状态发送
```
{
    logout:'true'
}
```
####服务器注销状态返回
```
{
    logout:'true'||logout:'false'
}
```
---------------
####报名表接口
`http://ccssbb.cn/applications/`

请求字段:
```
name
stu_num
phone
email
introduction
skill
want_learn
think_celitea
avatar
Authorization  //token 在请求头部
```
token认证失败即未登录状态返回  
`{'loginStatu':'fail'}`

报名成功返回  
`{'apply':'success'}`  

-------------
####添加文章接口
`http://ccssbb.cn/articles/`  
请求字段:
```
{'article':'xxx'}        //文章内容
{'Authorization':'token信息'}  #在请求头部
```

token认证失败即未登录状态返回  
`{'loginStatu':'fail'}`

非管理员文章添加失败  
`{'add_article':'fail'}`

管理员添加文章成功  
`{'add_article':'success'}`  

---------------------------
####查看报名列表接口
`http://ccssbb.cn/applylist/`  

get请求  
`{'Authorization':'token信息'}`  #在请求头部

`{'loginStatu':'fail'}`#非登录状态返回  

`{'isadmin':'no'}`  #非管理员返回  

成功将返回一个列表大概长这样:
```
[
    {
        'avatar_url':'xxx','create_time': 'Fri, 10 Aug 2018 09:40:22 GMT',
        'email':'chenshaobo@gmail.com',
        'introduction': 'xxx',
        'name': 'xxx',
        'phone': 2147483647,
        'skill': 'xxx',
        'stu_num': '16101202',
        'think_celitea': 'xxx',
        'user_id': 1,
        'want_learn': 'xxx'
    },
    {
        'avatar_url':'xxx',
        'create_time': 'Fri, 10 Aug 2018 09:42:29 GMT',  
        'email':'xxx',
        'introduction': 'xxx',
        'name': 'xxx',
        'phone': xxx,
        'skill': 'xxx',  
        'stu_num': 'xxx',
        'think_celitea': 'xxx',
        'user_id': 1,
        'want_learn': 'xxx'
    }
]
```

-------------------------
####申请短信验证码接口
`http://ccssbb.cn/sms/`

请求字段:  
`{'phone':'139xxxxxxxx'}`

申请成功返回:  
`'smsId':'ok'`  

失败返回:  
`'smsId':'这个是由第三方短信api提供者返回,是什么不记得了'`
