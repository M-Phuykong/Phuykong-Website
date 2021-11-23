from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Personal-Home"),
    path('contact/', views.contact, name="Personal-Contact"),
    path('about/', views.about, name="Personal-About")
]