"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.http import HttpResponseRedirect
from rest_framework.authtoken.views import obtain_auth_token
from users.views import UserView
from courses.views import CoursesView, CourseView
from jobs.views import JobsView
from webpages.views import WebPagesView

urlpatterns = [
    # Auth
    path('admin/', admin.site.urls),
    path("token/", obtain_auth_token),
    re_path("^auth/$", lambda request: HttpResponseRedirect("login/")),
    path("auth/", include("rest_framework.urls")),

    # Users endpoint
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/courses/", CoursesView.as_view()),
    path("users/<int:user_id>/jobs/", JobsView.as_view()),
    path("users/<int:user_id>/webpages/", WebPagesView.as_view()),

    # Courses endpoints
    path("courses/<int:course_id>/", CourseView.as_view()),

    # Jobs endpoints
    path("jobs/<int:job_id>", JobsView.as_view()),

    # Web page endpoints
    path("webpages/<int:webpage_id>", WebPagesView.as_view()),
]
