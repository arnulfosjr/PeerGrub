# Generated by Django 5.0.3 on 2024-04-22 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_listingratingstats_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="profile_image/"),
        ),
    ]
