from django.urls import path

from client.register import views

urlpatterns = [
    path(
        '',
        views.Index.as_view(),
        name='index'
    ),

    path(
        '<int:pk>/price',
        views.Price.as_view(),
        name='price'
    )
]
