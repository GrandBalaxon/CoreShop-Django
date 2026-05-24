from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.mixins import OwnerOrModeratorRequiredMixin
from catalog.models import ContactInfo, Product, Category
from catalog.services import ProductService


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


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailsView(DetailView):
    model = Product
    template_name = 'catalog/product_details.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()
        return render(self.request, "catalog/product_added.html")


class ProductUpdateView(LoginRequiredMixin, OwnerOrModeratorRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDeleteView(LoginRequiredMixin, OwnerOrModeratorRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/delete_confirm.html'
    success_url = reverse_lazy('catalog:products_list')
    context_object_name = "product"


class ProductPublicationStatusView(LoginRequiredMixin, View):
    """Отвечает за смену статуса публикации товара."""
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if product.owner == request.user or request.user.has_perm('catalog.can_unpublish_product'):
            product.is_published = not product.is_published
            product.save()

            return redirect("catalog:product_details", pk=pk)
        else:
            raise PermissionDenied


class CategoryProductsListView(DetailView):
    model = Category
    template_name = 'catalog/category_products.html'
    context_object_name = 'category'
