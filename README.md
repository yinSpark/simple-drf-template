# 简单 API 搭建模板

## 开发环境和工具

- 开发平台: Ubuntu 18.04
- 开发工具: VS Code
- 虚拟环境: pyenv

## 第三方模块安装

```
pip install django # django 3.0+
pip install djangorestframework # API 框架
pip install pygments # 实现代码的高亮显示
```

## 测试工具

- httpie

sudo apt-get  install httpie # 测试 Web API

- Postman

## 使用

pyenv 构建某一python 3 版本虚拟环境, 安装第三方模块。
运行项目

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py 
```

查看 <http://127.0.0.1:8000/>
