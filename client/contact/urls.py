from django.urls import path

from client.contact import views

urlpatterns = [
    path(
        '',
        views.Index.as_view(),
        name='index'
    ),

    path(
        '<str:email>/unsubscribe',
        views.Delete.as_view(),
        name='delete'
    )
]
