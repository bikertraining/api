from django.urls import path

from client.price import views

urlpatterns = [
    path(
        'search',
        views.Search.as_view(),
        name='search'
    ),
]
