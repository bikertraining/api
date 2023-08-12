from django.conf import settings
from django.conf.urls import include
from django.urls import path
from rest_framework.authtoken import models
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.response import Response

urlpatterns = [
    # Admin URLs
    path('admin/coach/', include('admin.coach.urls')),
    path('admin/contact/', include('admin.contact.urls')),
    path('admin/coupon/', include('admin.coupon.urls')),
    path('admin/ecourse/', include('admin.ecourse.urls')),
    path('admin/price/', include('admin.price.urls')),
    path('admin/schedule/', include('admin.schedule.urls')),

    # Client URLs
    path('client/contact/', include('client.contact.urls')),
    path('client/coupon/', include('client.coupon.urls')),
    path('client/ecourse/', include('client.ecourse.urls')),
    path('client/payment/', include('client.payment.urls')),
    path('client/price/', include('client.price.urls')),
    path('client/register/', include('client.register.urls')),
    path('client/schedule/', include('client.schedule.urls')),
    path('client/team/', include('client.team.urls')),
    path('client/whatsmyip/', include('client.whatsmyip.urls')),

    # Rest API Login
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]

# Debug Settings
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        # Debug Toolbar
        path('__debug__/', include(debug_toolbar.urls)),

        # API Documentation
        path('docs/', include_docs_urls(title='Documentation')),

        # DRF Login
        path('api-auth/', include('rest_framework.urls')),
    ]


# Custom Auth Token response
class CustomAuthToken(views.ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        token, created = models.Token.objects.get_or_create(user=user)

        return Response({
            'token': {
                'key': token.key
            }
        })


urlpatterns += [
    path('dj-rest-auth/api-token-auth/', CustomAuthToken.as_view())
]
