# Generated by Django 5.0 on 2024-05-04 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_alter_listing_listing_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Listing_Cost',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
