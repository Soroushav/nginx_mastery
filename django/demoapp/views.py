from django.shortcuts import render
from django.views.decorators.vary import vary_on_headers
from django.views.decorators.cache import cache_control
from django.utils.cache import patch_vary_headers


# @vary_on_headers('Accept-Language')
# def home(request):
#     return render(request, 'page1.html')

# @cache_control(public=True)
# def home(request):
#     return render(request, 'page1.html')


def home(request):
    response = render(request, 'page1.html')
    patch_vary_headers(response, newheaders=['User-Agent', 'Cookie'])
    print(type(response['Vary']))
    print(response['Vary'])
    return response