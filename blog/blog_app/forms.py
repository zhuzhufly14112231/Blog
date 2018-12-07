#!/usr/bin/env python
# encoding: utf-8
'''
@file: forms.py
@time: 2018/11/12 15:41
'''
from django import forms
from blog_app.models import Comment

# django 使用两个类来创建表单
# forms.Form 用于生成标准的表单
# form.ModelForm 用于从模型中生成表单

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
        # exclude 属性指定需要排除的字段
        # exclude = ('create',)

 