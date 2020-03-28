#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : yanglongyue
# @Time : 2020/3/26 0026 8:54

from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from utils import pager
############## 京城办CRM管理系统   收费记账统计模块#############
def count_excel(request):
    if request.method == "GET":
        name = request.user.username
        all_count = models.Company.objects.all().count()
        page_info = pager.PageInfo(request.GET.get('page'), all_count, 10, 'count_excel.html', 11)
        company_obj = models.Company.objects.all()[page_info.start():page_info.end()]
        return render(request,'count_excel.html',locals())
    else:

        kprice_end = request.POST.get("kprice_end",None)
        kant_name = request.POST.getlist("kant_name",None)
        title = request.POST.get("title",None)


        print(title)
        if title:
            print(title)
            all_count = models.Company.objects.filter(title__name__icontains=title).count()
            page_info = pager.PageInfo(request.GET.get('page'), all_count, 10, 'count_excel.html', 11)
            company_obj = models.Company.objects.filter(title__name__icontains=title)[page_info.start():page_info.end()]
            print(company_obj)
            name = request.user.username
            return render(request, 'count_excel.html', locals())
        if kprice_end:

            print(kprice_end)
            year = kprice_end.split('-')[0]
            print(year)
            month = kprice_end.split('-')[1]
            print(month)
            if month.startswith('0'):
                name = request.user.username
                print(month.split('0')[1])
                all_count = models.Company.objects.all().count()
                page_info = pager.PageInfo(request.GET.get('page'), all_count, 10, 'count_excel.html', 11)
                company_obj = models.Company.objects.filter(kprice_end__year=year, kprice_end__month=month.split('0')[1])[page_info.start():page_info.end()]
                return render(request, 'count_excel.html', locals())
            else:
                print(month)
                name = request.user.username
                all_count = models.Company.objects.all().count()
                page_info = pager.PageInfo(request.GET.get('page'), all_count, 10, 'count_excel.html', 11)
                company_obj = models.Company.objects.filter(kprice_end__year=year,kprice_end__month=month)[page_info.start():page_info.end()]
                return render(request, 'count_excel.html',locals())
        if kant_name:
            print(kant_name[0])
            name = request.user.username
            all_count = models.Company.objects.all().count()
            page_info = pager.PageInfo(request.GET.get('page'), all_count, 10, 'count_excel.html', 11)
            company_obj = models.Company.objects.filter(kans__name=kant_name[0])[page_info.start():page_info.end()]
            # for company_obj in company_objs:
            #     print(company_obj)
            return render(request, 'count_excel.html', locals())





def count_add(request):
    com_modlist = {'1':'小规模','2':'一般人'}
    if request.method =="GET":
        name = request.user.username
        company_obj = models.Company.objects.all()
        kant_obj = models.Kanter.objects.all()
        state_obj = models.ComState.objects.all()
        sole_obj = models.SoleUser.objects.all()
        return render(request,'count_add.html',locals())
    else:

        kant_name = request.POST.getlist("kant_name")
        title = request.POST.get("title")
        phone = request.POST.get("phone")
        cost_enddate = request.POST.get("cost_enddate")
        price_year = request.POST.get("price_year")
        state_id = request.POST.get("state")
        newpay_year = request.POST.get("newpay_year")
        price_month = request.POST.get("price_month")
        control_enddate = request.POST.get("control_enddate")
        control_price = request.POST.get("control_price")
        com_mod = request.POST.get("com_mod")
        kprice_start = request.POST.get("kprice_start")
        kprice_end = request.POST.get("kprice_end")
        remove_date = request.POST.get("remove_date")
        soles = request.POST.getlist("soles")
        buss_price = request.POST.get("buss_price")
        message = request.POST.get("message")
        print(request.POST)
        print(com_modlist[com_mod])

        company_add = models.Company.objects.create(title=title,phone=phone,cost_enddate=cost_enddate,price_year=price_year,state_id=state_id,
                                                    newpay_year=newpay_year,price_month=price_month,
                                                    control_enddate=control_enddate,
                                                    control_price=control_price,com_mod=com_modlist[com_mod],kprice_start=kprice_start,kprice_end=kprice_end,
                                                    remove_date=remove_date,buss_price=buss_price,message=message

                                                    )
        company_add.kans.add(*kant_name)
        company_add.soles.add(*soles)
        return redirect("/count_excel/")


def count_edit(request,id):
    company_obj = models.Company.objects.filter(nid=id).first()
    com_modlist = {'1': '小规模', '2': '一般人'}
    if request.method == "GET":
        name = request.user.username
        com_depart = models.ComDepart.objects.all()
        kant_obj = models.Kanter.objects.all()
        state_obj = models.ComState.objects.all()
        sole_obj = models.SoleUser.objects.all()
        print(company_obj.title.name)
        return render(request,'count_edit.html',locals())
    else:
        nid = request.POST.get("id")
        print(nid)
        kant_name = request.POST.getlist("kant_name")
        title = request.POST.get("title")
        phone = request.POST.get("phone")
        cost_enddate = request.POST.get("cost_enddate")
        price_year = request.POST.get("price_year")
        state_id = request.POST.get("state")
        newpay_year = request.POST.get("newpay_year")
        price_month = request.POST.get("price_month")
        control_enddate = request.POST.get("control_enddate")
        control_price = request.POST.get("control_price")
        com_mod = request.POST.get("com_mod")
        kprice_start = request.POST.get("kprice_start")
        kprice_end = request.POST.get("kprice_end")
        remove_date = request.POST.get("remove_date")
        soles = request.POST.getlist("soles")
        buss_price = request.POST.get("buss_price")
        message = request.POST.get("message")
        print(request.POST)
        print(com_modlist[com_mod])

        company_edit = models.Company.objects.filter(nid=id).update(title=title,phone=phone,cost_enddate=cost_enddate,price_year=price_year,state_id=state_id,
                                                    newpay_year=newpay_year,price_month=price_month,
                                                    control_enddate=control_enddate,
                                                    control_price=control_price,com_mod=com_modlist[com_mod],kprice_start=kprice_start,kprice_end=kprice_end,
                                                    remove_date=remove_date,buss_price=buss_price,message=message)
        company_obj.soles.set(soles)
        company_obj.kans.set(kant_name)
        return redirect("/count_excel/")


def count_del(request,id):
    print(request.POST)
    print(id)
    if id:
        models.Company.objects.filter(nid=id).delete()
        return redirect("/count_excel/")


############## 京城办CRM管理系统  会计人员管理模块#############

def kant_list(request):

    if request.method =="GET":
        name = request.user.username
        all_count = models.Kanter.objects.all().count()
        page_info = pager.PageInfo(request.GET.get('page'), all_count, 10, 'kant_list.html', 11)
        kant_obj = models.Kanter.objects.all()[page_info.start():page_info.end()]
        return render(request,'kant_list.html',locals())

def kant_add(request):
    if request.method =="GET":
        name = request.user.username

        return render(request,'kant_add.html',locals())
    else:
        kant_name = request.POST.get("kant_name")
        phone = request.POST.get("phone")

        models.Kanter.objects.create(name=kant_name,phone=phone)
        return redirect("/kant_list/")


def kant_edit(request,id):
    if request.method == "GET":
        name = request.user.username
        kant_obj = models.Kanter.objects.filter(nid=id).first()

        return render(request, 'kant_edit.html',locals())
    else:
        kant_name = request.POST.get("kant_name")
        phone = request.POST.get("phone")

        models.Kanter.objects.filter(nid=id).update(name=kant_name, phone=phone)
        return redirect("/kant_list/")


def kant_del(request,id):
    if id:
        models.Kanter.objects.filter(nid=id).delete()
        return redirect("/kant_list/")

############## 京城办CRM管理系统  客户公司管理模块#############


def comapny_list(request):

    if request.method =="GET":
        name = request.user.username
        all_count = models.ComDepart.objects.all().count()
        page_info = pager.PageInfo(request.GET.get('page'), all_count, 10, 'comapny_list.html', 11)
        comdepart_obj = models.ComDepart.objects.all()[page_info.start():page_info.end()]
        return render(request,'comapny_list.html',locals())

def comapny_add(request):
    if request.method =="GET":
        name = request.user.username

        return render(request,'company_add.html',locals())
    else:
        company_name = request.POST.get("title")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        models.ComDepart.objects.create(name=company_name,phone=phone,message=message)
        return redirect("/comapny_list/")


def comapny_edit(request,id):
    if request.method == "GET":
        name = request.user.username
        company_obj = models.ComDepart.objects.filter(nid=id).first()

        return render(request, 'company_edit.html',locals())
    else:
        company_name = request.POST.get("title")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        models.ComDepart.objects.filter(nid=id).update(name=company_name, phone=phone,message=message)
        return redirect("/comapny_list/")


def comapny_del(request,id):
    if id:
        models.ComDepart.objects.filter(nid=id).delete()
        return redirect("/comapny_list/")












if __name__ == '__main__':
    pass