from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.registration),
    path('login/', views.login),
    path('logout/', views.logout),
    path('products/', views.ProductListView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view()),
    path('orders/', views.OrderListView.as_view()),
    path('orders/<int:pk>/', views.OrderDetailView.as_view()),
    path('carts/', views.CartListView.as_view()),
    path('carts/<int:pk>/', views.CartDetailView.as_view())
]
