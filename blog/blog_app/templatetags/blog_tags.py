#!/usr/bin/env python
# encoding: utf-8
'''
@file: blog_tags.py
@time: 2018/11/13 14:13
'''
from django.db.models import Count
from django import template
from blog_app.models import Post

# 用来注册一个自定义的标签
register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog/post/lastest_posts.html')
def show_lastest_posts(count=2):
    lastest_posts = Post.published.order_by('-publish')[:count]
    return {'lastest_posts':lastest_posts}

@register.simple_tag
def num_count_posts():
    return Post.published.annotate(num_count=Count('author')).order_by('-num_count')

@register.simple_tag
def get_most_comments_posts():
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:2]

@register.filter
def post_add(num,noc):
    x = num+noc
    return x

@register.filter
def post_count(post):
    count = len(post.body)
    return count