from django.shortcuts import render

from catalog.models import ContactInfo, Product


def index(request):
    products = Product.objects.all()
    context = {'products': products}

    return render(request, 'catalog/index.html', context)


def contacts(request):
    contact_info = ContactInfo.objects.first()
    context = {'contact_info': contact_info}

    if request.method == 'POST':
        name = request.POST.get('name')
        context['name'] = name

        return render(request, "catalog/message_received.html", context)

    return render(request, 'catalog/contacts.html', context)


def product_details(request, product_id):
    data = Product.objects.get(id=product_id)
    context = {
        'product': data
    }
    return render(request, 'catalog/product_details.html', context)
