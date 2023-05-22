from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import CustomUserForm, CustomAdminForm, AppCreateForm
from .models import App, downloadApp, User, AdminUser, Profile
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# rest api import
from rest_framework import generics as rest_generics
from .serializers import AppSerializer, AdminSerializer, ProfileSerializer, UserSerializer, downloadAppSerializer
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from rest_framework.decorators import api_view
from django.contrib import messages
from django import forms


# admin authorisation

class CustomLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is the user is an admin user."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_admin:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


# class based views

class UserCreateVIew(generic.CreateView):
    form_class = CustomUserForm
    template_name = "app_promo/signup.html"

    def get_success_url(self):
        return reverse("login")


class AdminUserCreateView(generic.CreateView):
    form_class = CustomAdminForm
    template_name = "app_promo/admin_signup.html"

    def get_success_url(self):
        return reverse("login")


class AppListView(generic.ListView):
    model = App
    template_name = "app_promo/appz_list.html"
    paginate_by = 5
    ordering = ["-date"]


class AppCreateView(CustomLoginRequiredMixin, generic.CreateView):
    form_class = AppCreateForm

    template_name = "app_promo/app_create.html"

    def get_success_url(self):
        return reverse("admin_page")


@login_required
def profile(request):
    return render(request, 'app_promo/profile.html')


@login_required
def completed_tasks(request):
    user = request.user
    completed_apps = downloadApp.objects.filter(user=user)
    return render(
        request, "app_promo/completed_tasks.html", {"completed_apps": completed_apps}
    )


@login_required
def upload_document(request, pk):
    app = get_object_or_404(App, pk=pk)  # Retrieve the app based on the provided pk

    if request.method == "POST":
        file = request.FILES.get("file")
        user = request.user  # Assuming the user is authenticated
        # Create a DownloadApp instance and associate it with the user and app
        download_app = downloadApp.objects.create(app=app, user=user, screenshot=file)

        return redirect("profile")
    return render(request, "app_promo/download.html", {"app": app})


# rest api

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class AppApiCreateView(rest_generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = AppSerializer
    queryset = App.objects.all()


class AppApiListView(rest_generics.ListAPIView):
    serializer_class = AppSerializer
    queryset = App.objects.all()


class AdminUserListView(rest_generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AdminSerializer

    def get_queryset(self):
        user = self.request.user
        return AdminUser.objects.filter(username=user.username)


class AdminUserApiCreateView(rest_generics.CreateAPIView):
    serializer_class = AdminSerializer


class UserApiCreateView(rest_generics.CreateAPIView):
    serializer_class = UserSerializer


class UserApiListView(rest_generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=user.username)


# updateing screenshot


class DownloadAppApi(rest_generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = downloadAppSerializer
    queryset = downloadApp.objects.all()

    def perform_create(self, serializer):
        # Set the user field as the authenticated user
        serializer.save(user=self.request.user)


class DownloadAppListApi(rest_generics.ListAPIView):
    serializer_class = downloadAppSerializer
    queryset = downloadApp.objects.all()


class CompletedTaskListApi(rest_generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = downloadAppSerializer

    def get_queryset(self):
        user = self.request.user
        return downloadApp.objects.filter(user=user)



class ProfileCreateListApi(rest_generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)
