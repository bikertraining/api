from django.urls import path

from client.whatsmyip import views

urlpatterns = [
    path(
        '',
        views.Index.as_view(),
        name='index'
    )
]
