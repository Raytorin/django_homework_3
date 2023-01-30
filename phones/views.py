from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    filter_ = request.GET.get('sort')
    if filter_ == 'name':
        phones = Phone.objects.order_by(filter_)
    elif filter_ == 'low_price':
        phones = Phone.objects.order_by('price')
    elif filter_ == 'high_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone = Phone.objects.get(slug=slug)

    context = {
        'phone': phone
    }
    return render(request, template, context)
