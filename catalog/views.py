from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from catalog.models import ContactInfo, Product, Category


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = ContactInfo.objects.first()
        return context

    @staticmethod
    def post(request):
        name = request.POST.get('name')
        context = {'name': name}

        return render(request, 'catalog/message_received.html', context)


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
