"""BMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url

from app01.views import views,crm

urlpatterns = [
    url('^admin/', admin.site.urls),
    ############## 登录认证 #############
    url('^$', views.login),
    url('^login/', views.login),
    url('^index/', views.index),
    url('^reg/', views.reg),
    url('^logout/', views.logout),
    url('^set_password/', views.set_password),
    url('^zhuye/',views.zhuye),
    url('^shujia/',views.zhuye),
    url('^put/',views.file_put),
    ############## 京城办CRM管理系统  收费统计模块#############
    url('^put/',views.file_put),
    url('^count_excel/',crm.count_excel),
    url('^count_add/',crm.count_add),
    url('^count_edit/(\d+)/$',crm.count_edit),
    url('^count_del/(\d+)/$',crm.count_del),
    ############## 京城办CRM管理系统  会计人员管理模块#############

    url('^kant_list/',crm.kant_list),
    url('^kant_add/',crm.kant_add),
    url('^kant_edit/(\d+)/$',crm.kant_edit),
    url('^kant_del/(\d+)/$',crm.kant_del),
############## 京城办CRM管理系统  客户公司管理模块#############
    url('^comapny_list/',crm.comapny_list),
    url('^comapny_add/',crm.comapny_add),
    url('^comapny_edit/(\d+)/$',crm.comapny_edit),
    url('^comapny_del/(\d+)/$',crm.comapny_del),

]
