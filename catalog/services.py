from django.core.cache import cache
from catalog.models import Product


def get_products_by_category(category_id):
    """Возвращает список всех продуктов категории, отсортированных по цене."""
    cache_key = f'category_{category_id}'
    products = cache.get(cache_key)

    if products is None:
        products = list(Product.objects.filter(category_id=category_id).order_by('price'))
        cache.set(cache_key, products, timeout=60*15)

    return products
