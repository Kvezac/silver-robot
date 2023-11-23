from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def creat_paginator(request, items, result=6):
    page = request.GET.get('page')
    paginator = Paginator(items, result)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        items = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        items = paginator.page(page)
    page = int(page)
    left_index = page - 2 if page > 2 else 1
    right_index = page + 3 if page < paginator.num_pages - 2 else paginator.num_pages + 1
    custom_range = range(left_index, right_index)

    return items, paginator, custom_range
