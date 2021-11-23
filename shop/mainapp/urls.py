from django.urls import path

from .views import test_view, ProductDetailView, CategoryDetailView


urlpatterns = [
    path('', test_view, name='main_page'),
    path('product/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail' ),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
]
