from django.contrib import admin
from django.urls import path, include
from phone_auth_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('phone-auth/', include('phone_auth_app.urls')),
]
