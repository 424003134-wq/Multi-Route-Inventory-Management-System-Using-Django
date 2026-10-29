
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("item/<str:product_name>/", views.product_detail, name="product_detail"),
]
