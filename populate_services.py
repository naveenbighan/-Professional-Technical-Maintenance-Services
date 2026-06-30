"""
Management command to populate the database with default services.
Run with: python manage.py shell < populate_services.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bostan_website.settings')
django.setup()

from main.models import Service

services_data = [
    {
        'name': 'Alternative Energy Equipment Installation and Maintenance',
        'slug': 'alternative-energy-equipment',
        'short_description': 'Installation and maintenance support for alternative energy systems and equipment.',
        'detailed_description': 'We support alternative energy equipment with careful installation, inspection, and maintenance services for residential and commercial properties.',
        'icon': 'fas fa-solar-panel',
        'order': 1,
    },
    {
        'name': 'Floor & Wall Tiling Works',
        'slug': 'floor-wall-tiling-works',
        'short_description': 'Professional floor and wall tile installation, replacement, and repair services.',
        'detailed_description': 'Expert tile installation, replacement, and repair services for floors and walls, including ceramic, porcelain, marble, and mosaic tiles.',
        'icon': 'fas fa-th-large',
        'order': 2,
    },
    {
        'name': 'Carpentry & Wood Flooring Works',
        'slug': 'carpentry-wood-flooring-works',
        'short_description': 'Custom carpentry, wood flooring, fittings, and precision wood works.',
        'detailed_description': 'Custom carpentry and wood flooring solutions for residential and commercial interiors, delivered with accurate fitting and durable workmanship.',
        'icon': 'fas fa-hammer',
        'order': 3,
    },
    {
        'name': 'Engraving & Ornamentation Works',
        'slug': 'engraving-ornamentation-works',
        'short_description': 'Decorative engraving and ornamentation work for refined interior finishes.',
        'detailed_description': 'Decorative engraving and ornamentation works for interior surfaces, wood features, partitions, and finishing details.',
        'icon': 'fas fa-pen-nib',
        'order': 4,
    },
    {
        'name': 'Wallpaper Fixing Works',
        'slug': 'wallpaper-fixing-works',
        'short_description': 'Wallpaper fixing, replacement, and finish preparation for homes and offices.',
        'detailed_description': 'Professional wallpaper fixing and replacement with proper wall preparation, alignment, and finishing for clean interiors.',
        'icon': 'fas fa-scroll',
        'order': 5,
    },
    {
        'name': 'False Ceiling & Light Partitions Installation',
        'slug': 'false-ceiling-light-partitions',
        'short_description': 'False ceiling and light partition installation with neat, durable finishing.',
        'detailed_description': 'False ceiling and light partition installation for practical, polished interiors, including framing, fitting, and finishing coordination.',
        'icon': 'fas fa-border-all',
        'order': 6,
    },
    {
        'name': 'Electrical Fittings & Fixtures Repairing & Maintenance',
        'slug': 'electrical-fittings-fixtures-maintenance',
        'short_description': 'Repairing and maintenance for electrical fittings, fixtures, and related systems.',
        'detailed_description': 'Reliable repairing and maintenance for electrical fittings and fixtures, handled with attention to safety and performance.',
        'icon': 'fas fa-bolt',
        'order': 7,
    },
]

for service_data in services_data:
    service, created = Service.objects.get_or_create(
        slug=service_data['slug'],
        defaults=service_data
    )
    if created:
        print(f"Created service: {service.name}")
    else:
        print(f"Service already exists: {service.name}")

print(f"\nTotal services: {Service.objects.count()}")
