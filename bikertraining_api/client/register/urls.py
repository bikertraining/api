from django.urls import path

from client.register import views

urlpatterns = [
    path(
        'index',
        views.Index.as_view(),
        name='index'
    ),

    path(
        'price/<int:pk>',
        views.Price.as_view(),
        name='price'
    ),
]
