# APP Project

This repository contains the source code for the APP project, a web application developed using Django.

## Description

The APP project is a web application that allows users to perform various tasks related to app promotion. The application consists of two types of users: Admin User and Regular User.

- **Admin User**: Admin users have the ability to create app instances, specify app details such as name, category, and points. They can also upload an app icon and manage user profiles. Admin users are identified by the `is_admin` field set to `True` in the `AdminUser` model.

- **Regular User**: Regular users can view and download available app instances, upload screenshots of downloaded apps, and earn points associated with the app instances. The total points earned by regular users are displayed on their profiles.

## Installation

1. Clone the repository to your local machine:
git clone https://github.com/Amalsky/APP.git
3.Navigate to the project directory:
cd app-project
4.Create a virtual environment:
python3 -m venv env
5.Activate the virtual environment:
source env/bin/activate
6.Install the project dependencies:
pip install -r requirements.txt
7.Run database migrations:
python manage.py migrate
8.Start the development server:
python manage.py runserver
9.Access the application by visiting http://localhost:8000 in your web browser.

Project Structure
The project follows a standard Django project structure:
app_promo: Django app for handling app promotion-related functionality.
APP: Django project settings and configuration.
media: Directory for storing uploaded media files (e.g., app icons, screenshots).
static: Directory for storing static files (e.g., CSS, JavaScript).
templates: Directory for storing HTML templates.

User Models
The project includes two user models:

User Model
The User model represents regular users and extends Django's AbstractUser class. It has the following fields:
total_points: FloatField to store the total points earned by the user (default: 0).
is_admin: BooleanField indicating whether the user is an admin user or not (default: False).
AdminUser Model
The AdminUser model represents admin users and extends the User model. It has an additional method to handle saving admin users and a get_login_redirect_url method to specify the redirect URL after login.

App Model
The App model represents app instances and has the following fields:
app_name: CharField to store the app name (max length: 500).
app_category: CharField to store the app category (max length: 200) with predefined choices.
app_point: FloatField to store the points associated with the app (default: 0).
app_icon: ImageField to upload and store the app icon (default: "default.jpg").
date: DateTimeField to store the creation date of the app instance (default: current time).

DownloadApp Model
The DownloadApp model represents the screenshots uploaded by regular users. It has the following fields:
screenshot: ImageField to upload and store the screenshot image.
app: ForeignKey to the App model to associate the screenshot with the app instance.
user: ForeignKey to the User model to associate the screenshot with the user.
The save method of the DownloadApp model is overridden to add the points associated with the app to the user's total points when saving.

Profile Model
The Profile model represents user profiles and has a one-to-one relationship with the User model. It has the following field:
user: OneToOneField to associate the profile with the user.
image: ImageField to upload and store the profile image (default: "profile_default.jpg").
The Profile model is automatically created when a user is signed up using the create_profile and save_profile signals.

Forms
The project includes several forms for user registration and app creation:
CustomUserForm: UserCreationForm subclass for regular user registration.
CustomAdminForm: UserCreationForm subclass for admin user registration.
AppCreateForm: ModelForm for creating app instances, including fields for app name, category, points, and icon.

Views
The project includes both class-based views and function-based views for different functionalities:
Class-based views:
UserCreateView: CreateView subclass for regular user registration.
AdminUserCreateView: CreateView subclass for admin user registration.
AppListView: ListView subclass for displaying the list of available app instances.
AppCreateView: CreateView subclass for creating new app instances (restricted to admin users).
Function-based views:
profile: Renders the user profile page.
completed_tasks: Renders the completed tasks page showing the screenshots uploaded by the user.
upload_document: Handles the screenshot upload functionality.
REST API views:
AppApiCreateView: CreateAPIView subclass for creating new app instances via the REST API (restricted to admin users).
AppApiListView: ListAPIView subclass for retrieving a list of app instances via the REST API.
AdminUserListView: ListAPIView subclass for retrieving a list of admin users via the REST API (restricted to authenticated users).
AdminUserApiCreateView: CreateAPIView subclass for creating new admin users via the REST API.
UserApiCreateView: CreateAPIView subclass for creating new regular users via the REST API.
UserApiListView: ListAPIView subclass for retrieving a list of regular users via the REST API (restricted to authenticated users).
DownloadAppApi: CreateAPIView subclass for uploading screenshots via the REST API (restricted to authenticated users).
DownloadAppListApi: ListAPIView subclass for retrieving a list of uploaded screenshots via the REST API.
CompletedTaskListApi: ListAPIView subclass for retrieving a list of completed tasks (uploaded screenshots) via the REST API (restricted to authenticated users).
ProfileCreateListApi: ListAPIView subclass for retrieving a list of user profiles via the REST API (restricted to authenticated users).

License
The APP project is open-source and released under the MIT License.



