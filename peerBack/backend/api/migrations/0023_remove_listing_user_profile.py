# Generated by Django 5.0.3 on 2024-05-03 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0022_alter_listing_user_profile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="listing",
            name="user_profile",
        ),
    ]