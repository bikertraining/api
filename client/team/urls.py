from django.urls import path

from client.team import views

urlpatterns = [
    path(
        '',
        views.Index.as_view(),
        name='index'
    )
]
