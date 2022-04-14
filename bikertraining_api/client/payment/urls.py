from django.urls import path

from client.payment import views

urlpatterns = [
    path(
        'index',
        views.Index.as_view(),
        name='index'
    ),
]
