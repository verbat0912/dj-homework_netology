from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    s = request.GET.get('sort')
    if s == 'name':
        phones_all = Phone.objects.order_by('name')
    elif s == 'min_price':
        phones_all = Phone.objects.order_by('price')
    elif s == 'max_price':
        phones_all = Phone.objects.order_by('-price')
    else:
        phones_all = Phone.objects.all()
    context = {'phones' : phones_all}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone' : Phone.objects.get(slug = slug)}
    return render(request, template, context)