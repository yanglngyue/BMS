#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : yanglongyue
# @Time : 2020/3/22 0022 18:49


from django import forms

class BookForm(forms.Form):

    title = forms.CharField(max_length=32)
    price = forms.IntegerField()
    email = forms.EmailField()


















if __name__ == '__main__':
    pass