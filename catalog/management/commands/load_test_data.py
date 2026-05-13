from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection

from blog.models import BlogPost, Category as BlogCategory
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add test categories and products to the database.'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        BlogPost.objects.all().delete()
        BlogCategory.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE blog_blogpost_id_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE blog_category_id_seq RESTART WITH 1;")

        call_command('loaddata', 'catalog_fixture.json')

        self.stdout.write(self.style.SUCCESS('Test data loaded successfully.'))
