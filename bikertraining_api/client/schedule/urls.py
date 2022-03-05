from django.urls import path

from client.schedule import views

urlpatterns = [
    path(
        'search',
        views.Search.as_view(),
        name='search'
    )
]
