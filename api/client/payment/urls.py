from django.urls import path

from client.payment import views

urlpatterns = [
    path(
        '',
        views.Index.as_view(),
        name='index'
    ),

    path(
        '<str:class_type>/price',
        views.Price.as_view(),
        name='price'
    )
]
