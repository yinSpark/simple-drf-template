# 使用 Django 开发 API

使用 DRF 开发一个简单的代码高亮显示的 Web API

## 一、准备工作

使用虚拟环境开发

```
pip install django
pip install djangorestframework
pip install pygments # 实现代码的高亮显示

sudo apt-get  install httpie # 测试 Web API
```

## 二、基础设置

1. 创建项目 tutorial
2. 创建 app (snippets)
3. 注册app
将 'rest_framework' 和 'snippets' 注册

## 三、创建模型

基本模型 --> 添加认证限制和高亮显示

## 四、创建序列化类

基本序列化类 --> 使用 ModelSerializer

## 五、创建视图

基本函数视图 --> 使用 @api_view 装饰基于函数的视图 --> 使用APIView 基于类的视图 --> 使用 Mixins 混入类 --> 使用组合类视图 --> 使用 ViewSets 进行重构

## 六、注册路由

基本路由 --> ViewSets 绑定到具体视图，再注册路由 --> 使用 Routers 自动化 URL 配置

## 七、测试
