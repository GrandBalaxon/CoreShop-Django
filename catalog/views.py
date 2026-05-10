from django.shortcuts import render

from catalog.models import ContactInfo, Product, Category


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


def add_product(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        new_product = Product.objects.create(
            name=name,
            price=price,
            category_id=category_id,
            description=description,
            image=image,
        )

        return render(request, "catalog/product_added.html")

    return render(request, 'catalog/add_product.html', context)
