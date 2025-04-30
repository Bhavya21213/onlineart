from django.contrib import admin
from django.urls import path,include
from online import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('about', views.home, name = 'home'),
    path('services',views.product, name = 'product'),
    path('contact' , views.contact, name = 'contact'),
    path('login' , views.login, name = 'login'),

]