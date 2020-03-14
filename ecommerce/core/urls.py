from django.urls import path, include
from .views import HomeView, ItemDetailView, checkout, add_to_cart


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add_to_cart/<slug>/', add_to_cart, name = 'add_to_cart')
]
