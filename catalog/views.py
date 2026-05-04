from django.shortcuts import render

from catalog.models import ContactInfo, Product


def index(request):
    latest_products = Product.objects.order_by('-created_at')[:5]

    print("Последние 5 продуктов:")
    for product in latest_products:
        print(f"* {product.name} — ${product.price} - Категория: {product.category}")

    return render(request, 'catalog/index.html')


def contacts(request):
    contact_info = ContactInfo.objects.first()
    context = {'contact_info': contact_info}

    if request.method == 'POST':
        name = request.POST.get('name')
        context['name'] = name

        return render(request, "catalog/message_received.html", context)

    return render(request, 'catalog/contacts.html', context)
