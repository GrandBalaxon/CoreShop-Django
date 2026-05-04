from django.core.management import call_command
from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add test categories and products to the database.'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'catalog_fixture.json')

        self.stdout.write(self.style.SUCCESS('Test data loaded successfully.'))
