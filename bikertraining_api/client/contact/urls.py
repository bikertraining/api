from django.urls import path

from client.contact import views

urlpatterns = [
    path(
        'index',
        views.Index.as_view(),
        name='index'
    ),

    path(
        'unsubscribe/<str:email>',
        views.Delete.as_view(),
        name='delete'
    )
]
