from django.urls import path

from admin.coach import views

urlpatterns = [
    path(
        'create',
        views.Create.as_view(),
        name='create'
    ),

    path(
        'delete/<int:pk>',
        views.Delete.as_view(),
        name='delete'
    ),

    path(
        'edit/<int:pk>',
        views.Edit.as_view(),
        name='edit'
    ),

    path(
        'search',
        views.Search.as_view(),
        name='search'
    )
]
