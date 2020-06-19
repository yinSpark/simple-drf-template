## 一、FBV 和 CBV 区别

> url(路由) -->父类as_view() (1、实例化对象；2、通过dispatch()反射找到具体方法

> get/post/put/delete/patch/head/option/trace  

> 多个类有共同方法，定义基类，通过继承实现

## 二、django 中间件
> process_request
> process_view
> process_response
> process_exception
> process_render_template

执行过程
```
请求-->所有 request --> 路由匹配 --> 跳回来 --> 执行所有view --> 执行view函数 --> 执行所有 response -->返回
```

中间件做什么

- 权限
- 用户登录验证
- django 的 csrf 是如何实现的(process_view)
原理：用户发post请求要携带发送的随机字符串
> process_view() 功能
> > 1）检查视图是否被装饰 @csrf_except/@csrf_protect
> > 2）去请求体或 cookie中获取 token

CBV 使用 crsf 时
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator

加装饰器时
> 1. 加在dispatch()方法上@method_decorator(csrf_exempt)
> 2. 加载类上@method_decorator(csrf_exempt, name='dispatch')