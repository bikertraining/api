from django.urls import path

from client.ecourse import views

urlpatterns = [
    path(
        'search',
        views.Ecourse.as_view(),
        name='ecourse'
    )
]
