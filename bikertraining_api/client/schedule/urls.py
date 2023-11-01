from django.urls import path

from client.schedule import views

urlpatterns = [
    path(
        'search',
        views.Search.as_view(),
        name='search'
    ),

    path(
        'search/<str:class_type>',
        views.SearchByType.as_view(),
        name='search-by-type'
    ),

    path(
        '<int:id>',
        views.SearchById.as_view(),
        name='search-by-id'
    )
]
