from django.urls import path

from admin.ecourse import views

urlpatterns = [
    path(
        'search',
        views.Ecourse.as_view(),
        name='ecourse'
    )
]
