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
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from courses.views import CourseViewSet
from jobs.views import JobViewSet
from webpages.views import WebPageViewSet
from rest_framework.routers import DefaultRouter

# create a router that registers the endpoints for the resources
router = DefaultRouter()
router.register("courses", CourseViewSet)
router.register("jobs", JobViewSet)
router.register("webpages", WebPageViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),  # page for django admin
    path("token/", obtain_auth_token),  # page for token access
    path("auth/", include("rest_framework.urls")),  # non admin login portal
] + router.urls  # adds all the URLs from the router
