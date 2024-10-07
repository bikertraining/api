from django.urls import path

from admin.register import views

urlpatterns = [
    path(
        '<int:schedule>/<int:pk>/print',
        views.Print.as_view(),
        name='print'
    ),

path(
        '<int:schedule>/search',
        views.Search.as_view(),
        name='search'
    )
]
