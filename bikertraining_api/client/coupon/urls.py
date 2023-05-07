from django.urls import path

from client.coupon import views

urlpatterns = [
    path(
        'search',
        views.Search.as_view(),
        name='search'
    ),

    path(
        'validate/<str:name>/<str:class_type>',
        views.Validate.as_view(),
        name='validate'
    ),
]
