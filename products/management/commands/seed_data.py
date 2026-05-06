"""
Management command to populate the database with sample categories and products.
Run: python manage.py seed_data
"""

from django.core.management.base import BaseCommand
from products.models import Category, Product
from decimal import Decimal


SAMPLE_DATA = [
    {
        "category": "Electronics",
        "products": [
            {
                "name": "Wireless Noise-Cancelling Headphones",
                "description": "Premium over-ear headphones with active noise cancellation, 30-hour battery life, and superior sound quality. Perfect for music lovers and remote workers alike.",
                "price": Decimal("89.99"),
                "stock": 25,
            },
            {
                "name": "Portable Bluetooth Speaker",
                "description": "Compact 360° waterproof speaker with rich bass, 12-hour playtime, and built-in microphone. Your perfect outdoor companion.",
                "price": Decimal("49.99"),
                "stock": 40,
            },
            {
                "name": "USB-C Fast Charging Hub",
                "description": "7-in-1 USB-C hub with 4K HDMI, 100W PD charging, SD card reader, and 3 USB-A ports. Works with all modern laptops.",
                "price": Decimal("34.99"),
                "stock": 60,
            },
        ],
    },
    {
        "category": "Clothing",
        "products": [
            {
                "name": "Classic Slim-Fit T-Shirt",
                "description": "100% premium cotton, pre-shrunk slim-fit t-shirt available in multiple colours. Breathable, soft, and built to last.",
                "price": Decimal("19.99"),
                "stock": 120,
            },
            {
                "name": "Lightweight Zip Hoodie",
                "description": "Versatile zip-up hoodie crafted from a cotton-polyester blend. Features kangaroo pockets and a flattering modern cut.",
                "price": Decimal("44.99"),
                "stock": 55,
            },
            {
                "name": "Stretch Denim Jeans",
                "description": "5-pocket slim-straight jeans with 2% elastane for all-day comfort. Classic styling that pairs with everything.",
                "price": Decimal("59.99"),
                "stock": 80,
            },
        ],
    },
    {
        "category": "Books",
        "products": [
            {
                "name": "Clean Code: A Handbook of Agile Software Craftsmanship",
                "description": "Robert C. Martin's seminal guide to writing readable, maintainable code. A must-read for every professional developer.",
                "price": Decimal("29.99"),
                "stock": 30,
            },
            {
                "name": "The Pragmatic Programmer",
                "description": "20th Anniversary Edition. Timeless advice for software developers on craftsmanship, productivity, and career growth.",
                "price": Decimal("34.99"),
                "stock": 20,
            },
        ],
    },
    {
        "category": "Home & Kitchen",
        "products": [
            {
                "name": "Stainless Steel French Press",
                "description": "34 oz double-walled French press that keeps coffee hot for hours. No plastic parts — easy to clean and built to last.",
                "price": Decimal("27.99"),
                "stock": 45,
            },
            {
                "name": "Bamboo Cutting Board Set",
                "description": "Set of 3 eco-friendly bamboo cutting boards in different sizes. Naturally antimicrobial, dishwasher-safe, and gorgeous on any counter.",
                "price": Decimal("24.99"),
                "stock": 70,
            },
        ],
    },
]


class Command(BaseCommand):
    help = 'Seeds the database with sample categories and products'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.MIGRATE_HEADING('Seeding sample data...'))

        created_categories = 0
        created_products   = 0

        for group in SAMPLE_DATA:
            category, cat_created = Category.objects.get_or_create(
                name=group['category']
            )
            if cat_created:
                created_categories += 1
                self.stdout.write(f'  [+] Category: {category.name}')

            for pdata in group['products']:
                product, prod_created = Product.objects.get_or_create(
                    name=pdata['name'],
                    defaults={
                        'category':    category,
                        'description': pdata['description'],
                        'price':       pdata['price'],
                        'stock':       pdata['stock'],
                        'available':   True,
                    }
                )
                if prod_created:
                    created_products += 1
                    self.stdout.write(f'      -> Product: {product.name} (${product.price})')

        self.stdout.write(
            self.style.SUCCESS(
                f'\nDone! Created {created_categories} categories and {created_products} products.'
            )
        )
        self.stdout.write(
            self.style.WARNING(
                'Tip: Run "python manage.py createsuperuser" to create an admin account.'
            )
        )
