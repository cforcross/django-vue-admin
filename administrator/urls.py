from django.urls import path,include
from .views import (AmbassadorAPiView,ProductGenericApiView,LinkAPiView,
OrderAPIView)

urlpatterns = [
    path('',include('common.urls')),
    path('ambassadors',AmbassadorAPiView.as_view()),
    path('products',ProductGenericApiView.as_view()),
    path('products/<str:pk>',ProductGenericApiView.as_view()),
    path('products/<str:pk>/links',LinkAPiView.as_view()),
    path('orders',OrderAPIView.as_view()),
]