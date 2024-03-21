from django.urls import path

from admin.coach import views

urlpatterns = [
    path(
        'create',
        views.Create.as_view(),
        name='create'
    ),

    path(
        '<int:pk>/delete',
        views.Delete.as_view(),
        name='delete'
    ),

    path(
        '<int:pk>/edit',
        views.Edit.as_view(),
        name='edit'
    ),

    path(
        'search/active',
        views.SearchActive.as_view(),
        name='search'
    ),

    path(
        'search/inactive',
        views.SearchInactive.as_view(),
        name='search'
    )
]
