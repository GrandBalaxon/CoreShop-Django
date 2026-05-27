from catalog.models import Category


def footer_categories(request):
    """Передаёт список всех категорий для футера."""
    return {
        'footer_categories': Category.objects.all()
    }
