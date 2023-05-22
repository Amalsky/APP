import django.apps
from django.contrib import admin
from .models import downloadApp, App, Profile, User
from django import forms


class AppAdmin(admin.AdminSite):
    site_header = "APP ADMIN"
    site_title = "App ADMIN"
    login_template = 'app_promo/admin.html'


blog_site = AppAdmin(name="AppAdmin")


class AppForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppForm, self).__init__(*args, **kwargs)
        self.fields['app_link'].help_text = 'enter app link'

    class Meta:
        model = App
        exclude = ('',)


class AppFormAdmin(admin.ModelAdmin):
    form = AppForm
    fields = ['app_name', 'app_link', ('app_point', 'app_icon')]


blog_site.register(App, AppFormAdmin)

# # automatic registering models
#
# models = django.apps.apps.get_models()
#
# for model in models:
#     try:
#
#         blog_site.register(model)
#
#     except blog_site.AlreadyRegistered:
#         pass
