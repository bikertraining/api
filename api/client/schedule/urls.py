from django.urls import path

from client.schedule import views

urlpatterns = [
    path(
        'search',
        views.Search.as_view(),
        name='search'
    ),

    path(
        'search/<int:id>/id',
        views.SearchById.as_view(),
        name='search-by-id'
    ),

    path(
        'search/<str:class_type>/type',
        views.SearchByType.as_view(),
        name='search-by-type'
    )
]
