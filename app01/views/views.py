from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# from app01.models import Book, Publish, Author, AuthorDetail
from utils.pager import *
from django.contrib import auth

from django.contrib.auth.models import User

# from app01.models import UserInfo

import json

##################### 图书管理系统 视图函数 ##################


# def book_list(request):
#
#     if request.method == "GET":
#         name = request.user.username
#         all_count = Book.objects.all().count()
#         page_info = PageInfo(request.GET.get('page'), all_count, 10, 'book_view.html', 11)
#         Book_list = Book.objects.all()[page_info.start():page_info.end()]
#
#
#         return render(request, "book_view.html",{'Book_list':Book_list,'page_info':page_info,'name':name})
#     else:
#         search = request.POST.get("search")
#         print('搜索内容:', search)
#         book_list = Book.objects.filter(title__icontains=search)
#         return render(request, "book_view.html", {"book_list": book_list})
#
#
# def book_add(request):
#     if request.method == "GET":
#
#
#         name = request.user.username
#
#         publish_list = Publish.objects.all()
#         author_list = Author.objects.all()
#         return render(request, "book_add.html", {"publish_list": publish_list, "author_list": author_list,"name":name})
#     else:
#         title = request.POST.get("title")
#         price = request.POST.get("price")
#         pub_date = request.POST.get("pub_date")
#         publish_id = request.POST.get("publish_id")
#         authors = request.POST.getlist("authors")
#         print(request.POST)
#         print(authors)
#
#         book = Book.objects.create(title=title, price=price, pub_date=pub_date, publish_id=publish_id)
#         book.authors.add(*authors)
#
#         return redirect("/books/")
#
#
# def book_edit(request, edit_book_id):
#     edit_book = Book.objects.filter(pk=edit_book_id).first()
#     if request.method == "GET":
#
#         name = request.user.username
#
#         publish_list = Publish.objects.all()
#         author_list = Author.objects.all()
#         return render(request, "book_edit.html",
#                       {"edit_book": edit_book, "publish_list": publish_list, "author_list": author_list,"name":name})
#
#     else:
#         title = request.POST.get("title")
#         price = request.POST.get("price")
#         pub_date = request.POST.get("pub_date")
#         publish_id = request.POST.get("publish_id")
#         authors = request.POST.getlist("authors")
#         print(request.POST)
#         print(authors)
#         Book.objects.filter(pk=edit_book_id).update(title=title, price=price, pub_date=pub_date, publish_id=publish_id)
#         edit_book.authors.set(authors)
#
#         return redirect("/books/")
#
#
# def book_del(request, del_book_id):
#     response = {"state": True}
#     try:
#         Book.objects.filter(pk=del_book_id).delete()
#     except Exception as e:
#         json.dumps(response)
#
#     return HttpResponse(json.dumps(response))
#
# def publish(request):
#
#
#     name = request.user.username
#     publish= Publish.objects.all()
#
#     return render(request, "publish.html", {"publish_list": publish,"name":name})
#
#
# def publish_add(request):
#     if request.method == "GET":
#         name = request.user.username
#         publish_obj = Publish.objects.all()
#         return render(request, "publish_add.html",{"name":name,'publish_obj':publish_obj})
#
#
# def publish_edit(request,publish_id):
#     edit_publish = Publish.objects.filter(pk=publish_id).first()
#     if request.method == "GET":
#         if not request.user.is_authenticated:
#             return redirect("/login/")
#
#         name = request.user.username
#         return render(request, "publish_edit.html",
#                       {"edit_publish": edit_publish,"name":name})
#
#     else:
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#
#
#         Publish.objects.filter(pk=publish_id).update(name=name, email=email)
#
#
#         return redirect("/publish/")
#
#
# def publish_del(request,publish_id):
#
#     Publish.objects.filter(pk=publish_id).delete()
#
#     return redirect("/publish/")


def zhuye(request):
    print(request.user.is_authenticated)


    name = request.user.username


    return render(request, "zhuye.html",locals())


def index(request):
    name = request.user.username
    return render(request, "zhuye.html", locals())


def login(request):
    next_url = request.GET.get("next")

    if request.method=="POST":
        name = request.user.username

        user = request.POST.get('username')
        pwd = request.POST.get('pwd')
        # 数据库查询该用户是否存在
        # authenticate去auth_user查询记录，查询成功返回用户对象，查询失败返回None
        user_obj = auth.authenticate(username=user, password=pwd)
        # user_obj = UserInfo.objects.filter(user=user,pwd=pwd).first()
        if user_obj:
            print(next_url)
            # 保存用户状态信息
            auth.login(request, user_obj)  # request.session["user_id"]=user_obj.pk

            # request.session["user_id"] = user_obj.pk
            # 重定向index
            return HttpResponse(1)

        else:
            return HttpResponse(0)
    else:


        return  render(request,"denglu.html")

import os
from BMS import settings

def file_put(request):
    if request.method == "GET":
        name = request.user.username

        return render(request,"file_put.html",locals())

    else:
        print(request.POST)
        print(request.FILES)
        file_obj=request.FILES.get("file_obj")
        # 文件对象有一个name属性，获取文件名称字符串
        print(file_obj.name)
        path=file_obj.name

        path=os.path.join(settings.BASE_DIR,"media","img",path)
        with open(path,"wb") as f:
            for line in file_obj:
                f.write(line)


        return HttpResponse("OK")

def reg(request):


        user=request.POST.get("user")
        pwd=request.POST.get("pwd")

        User.objects.create_user(username=user,password=pwd)
        return HttpResponse(1)

def logout(request):

    auth.logout(request)

    return redirect("/login/")

def set_password(request):


    if request.method == "GET":
        name = request.user.username
        return render(request,"set_pwd.html",locals())
    else:
        user = User.objects.get(username=request.user.username)
        pwd = request.POST.get('new_pwd')
        user.set_password(raw_password=pwd)
        user.save()
        return redirect("/login/")
