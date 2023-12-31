# Generated by Django 4.2.1 on 2023-05-20 11:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app_promo", "0009_app_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="app",
            name="app_link",
        ),
        migrations.AddField(
            model_name="app",
            name="app_category",
            field=models.CharField(
                choices=[
                    ("SN", "Social Networking"),
                    ("ENT", "Entertainment"),
                    ("PROD", "Productivity"),
                    ("EDU", "Education"),
                    ("FIT", "Health & Fitness"),
                    ("TRAV", "Travel"),
                    ("FIN", "Finance"),
                    ("NEWS", "News & Magazines"),
                    ("MUSIC", "Music"),
                    ("PHOTO", "Photography"),
                    ("SHOP", "Shopping"),
                    ("GAME", "Games"),
                    ("SPORT", "Sports"),
                    ("UTIL", "Utilities"),
                    ("WEATH", "Weather"),
                    ("FOOD", "Food & Drink"),
                    ("LIFE", "Lifestyle"),
                    ("BUS", "Business"),
                ],
                default=django.utils.timezone.now,
                max_length=100,
            ),
            preserve_default=False,
        ),
    ]
