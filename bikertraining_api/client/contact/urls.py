from django.urls import path

from client.contact import views

urlpatterns = [
    path(
        'index',
        views.Index.as_view(),
        name='index'
    )
]
