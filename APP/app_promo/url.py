from django.urls import path, include
from django.contrib.auth import views as auth_view
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    # user signup url
    path("signup/", views.UserCreateVIew.as_view(), name="signup"),

    # admin signup url
    path("signup/admin/", views.AdminUserCreateView.as_view(), name="signup_admin"),

    # login url  both user and admin user will be redirected to home page
    path(
        "login/",
        auth_view.LoginView.as_view(template_name="app_promo/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_view.LogoutView.as_view(template_name="app_promo/logout.html"),
        name="logout",
    ),
    # uploading screenshot url
    path("<int:pk>/", views.upload_document, name="upload_document"),

    # home page
    path("", views.AppListView.as_view(), name="list"),

    # where admin user can create an App instance  page will be redircted to same page
    path("admin_page/", views.AppCreateView.as_view(), name="admin_page"),

    # list of complete tasked by the loged in user
    path("completed-tasks/", views.completed_tasks, name="completed_tasks"),

    # profile url
    path("profile/", views.profile, name="profile"),

    # DJANGO REST FRAMEWORK URLS

    path('api-auth/', include('rest_framework.urls')),

    # generate authentication token(username,password)
    path('api/token/', obtain_auth_token, name='authtoken'),

    # creating a App, user must be a adminuser(authentication token)
    path('app/create_api/', views.AppApiCreateView.as_view(), name='app_api_create'),

    # retrieving all apps instance
    path('app/list_api/', views.AppApiListView.as_view(), name='app_api_list'),

    # creating an adminuser
    path('app/create_admin_api/', views.AdminUserApiCreateView.as_view(), name='create_admin_api'),

    # retrieving adminuser credential(authentication token)
    path('app/list_admin_api/', views.AdminUserListView.as_view(), name='list_admin_api'),

    # creating a user
    path('app/create_user_api/', views.UserApiCreateView.as_view(), name='create_user_api'),

    # retrieving  login user credential(authentication token)
    path('app/list_user_api/', views.UserApiListView.as_view(), name='list_user_api'),

    # retrieving profile of logged-in user(authentication token)
    path('api/list_profile/', views.ProfileCreateListApi.as_view(), name='api_create_profile'),

    # uploading screenshot app id  must be passed  and user must be logged in(authentication token)
    path('api/upload_screenshot/', views.DownloadAppApi.as_view(), name='api_dowload_app'),

    # retrieving all screenshots from database use this retrieve app id
    path('api/retrieve_screenshot/', views.DownloadAppListApi.as_view(), name='api_dowload_app'),

    # retrieving all completed task by the logged-in user(authentication token)
    path('api/completed_task/', views.CompletedTaskListApi.as_view(), name='api_completed_task')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
