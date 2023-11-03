from django.urls import path

from client.fraud import views

urlpatterns = [
    path(
        '<str:name>/search/<str:fraud_type>',
        views.Search.as_view(),
        name='search'
    )
]
