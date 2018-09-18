
from django.contrib import admin
from django.urls import include, path
from todolist import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todolist.urls')),
]
