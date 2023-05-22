from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    total_points = models.FloatField(default=0)
    is_admin = models.BooleanField(default=False)


class AdminUser(User):
    def save(self, *args, **kwargs):
        self.is_admin = True
        super().save(*args, **kwargs)

    def get_login_redirect_url(self):

        return reverse('admin_page')


class App(models.Model):
    choices = [
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
    ]

    app_name = models.CharField(max_length=500)
    app_category = models.CharField(max_length=200, choices=choices)
    app_point = models.FloatField(default=0)
    app_icon = models.ImageField(upload_to="app_icon.jpg", default="default.jpg")
    date = models.DateTimeField(default=timezone.now)


# this model handles  screenshot updated by users  user will be only award points if screenshot is updated
class downloadApp(models.Model):
    screenshot = models.ImageField(upload_to="app_icon.jpg")
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # adding point's to user profile  overwriting the save method  since user field is ForeignKey to user field
    # retrieving User model total_point field and adding points
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Add points to the user here
        self.user.total_points += self.app.app_point
        self.user.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='app_icon.jpg', default="profile_default.jpg")
