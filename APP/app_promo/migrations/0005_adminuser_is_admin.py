# Generated by Django 4.2.1 on 2023-05-18 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_promo", "0004_adminuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="adminuser",
            name="is_admin",
            field=models.BooleanField(default=True),
        ),
    ]