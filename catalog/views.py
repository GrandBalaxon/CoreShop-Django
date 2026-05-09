from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView

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


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'catalog/product_details.html'
    context_object_name = 'product'


class AddProductView(CreateView):
    model = Product
    fields = ['name', 'price', 'category', 'description', 'image']
    template_name = 'catalog/add_product.html'

    def get_context_data(self, **kwargs):
        context = {
            'categories': Category.objects.all(),
        }
        return context

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, "catalog/product_added.html")
