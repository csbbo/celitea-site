目标url:celitea.cn

主页
```
get "/"
return{
    data
}
```
注册
```
post "/regist/" args(userName,userPassword,userPhoneNumber,userIdentifyingCode)
return{
    {'registerStatus':'phone_was_us'}
    or
    {'registerStatus':'success'}
    or
    {'registerStatus':'wrongCode'}
}

```
登录
```
post "/login/" args(userPhoneNumber,userPassword)
return{
    {'userName':user.username,'userRole':user.role.id,'token':token}
    or
    {'login':'fail'}
}
```
报名
```
post "/applications/" args(name,stu_num,phone,email,introduction,skill,want_learn,think_celitea) header(Authorization)
return{
    {'applications':'success'}
    or
    {'applications':'apply_exist'}
    or
    {'applications':'noLogin'}
}
```
查看报名列表
```
post "/apply_list/" args(apply_state) header(Authorization)
return{
    data
    or
    {'apply_list':'permissiondeny'}
    or
    {'apply_list':'noLogin'}
}
>apply_state="all_apply"    #请求所有报名表
>apply_state="notpass_apply"    #请求未通过报名表
>apply_state="all_apply"    #请求已经通过报名表
>apply_list = 其他            #请求待处理报名表
```
同意申请
```
post "/apply_pass/" args(apply_id) header(Authorization)
return{
    {'apply_pass':'sucess'}
    or
    {'apply_pass':'permissiondeny'}
    or
    {'apply_pass':'noLogin'}
}
```
拒绝申请
```
post "/apply_notpass/" args(apply_id) header(Authorization)
return{
    {'apply_notpass':'success'}
    or
    {'apply_notpass':'permissiondeny'}
    or
    {'apply_notpass':'noLogin'}
}
```

查看某个报名表内容
```
post "/apply_detail/" args(apply_id) header(Authorization)
return{
    data
    or
    {'apply_detail':'permissiondeny'}
    or
    {'apply_detail':'noLogin'}
}
```
添加文章
```
post "/add_articles/" args(article) header(Authorization)
return{
    {'add_article':'success'}
    or
    {'add_article':'permissiondeny'}
    or
    {'add_article':'noLogin'}
}
```
修改文章
```
post "/modify_article/" args(article,article_id)  header(Authorization)
return{
    {'modify_article':'formal_error'}
    or
    {'modify_article':'success'}
    or
    {'modify_article':'permissiondeny'}
    or
    {'modify_article':'noLogin'}
}
```
获取某一篇文章及其上一篇和下一篇文章
```
post "/article_detail/" args(article_id)
return{
    data
}
```

获取文章列表
```
# 可以从首页接口提取
```
添加个人简介
```
post "/add_bio/" args(bio) header(Authorization)
return{
    {'add_bio':'sucess'}
    or
    {'add_bio':'noLogin'}
}
```
添加和修改用户头像
```
post "/upload_avatar/" args(avatar) header(Authorization)
return{
    {'upload_avatar':'sucess'}
    or
    {'upload_avatar':'noLogin'}
}
```
将用户设置为成员
```
post "/to_member/" args(user_id) header(Authorization)
return{
    {'to_member':'success'}
    or
    {'to_member':'permissiondeny'}
    or
    {'to_member':'noLogin'}
}
```
申请验证码
```
post "/sms/" args(phone)
return{
    data
}
```
用户列表
```
get "/user_list/" header(Authorization)
return{
    data
    or
    {'user_list':'permissiondeny'}
    or
    {'user_list':'noLogin'}
}
```
用户信息
```
get "/user_detail/" header(Authorization)
return{
    data
    or
    {'user_detail':'noLogin'}
}
```
