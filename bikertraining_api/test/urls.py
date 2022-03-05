from django.urls import path

from test import views

urlpatterns = [
    path(
        'index',
        views.Index.as_view(),
        name='index'
    ),

    path(
        'test',
        views.test,
        name='test'
    )
]
