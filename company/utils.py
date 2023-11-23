from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def creat_paginator(request, item):
    page = request.GET.get('page')
    result = 6
    paginator = Paginator(item, result)
    try:
        item = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        item = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        item = paginator.page(page)
    page = int(page)
    left_index = page - 2 if page > 2 else 1
    right_index = page + 3 if page < paginator.num_pages - 2 else paginator.num_pages + 1
    custom_range = range(left_index, right_index)

    return paginator, custom_range
