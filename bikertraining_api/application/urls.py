from django.conf import settings
from django.conf.urls import include
from django.urls import path
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # Admin URLs
    path('admin/coach/', include('admin.coach.urls')),
    path('admin/price/', include('admin.price.urls')),
    path('admin/schedule/', include('admin.schedule.urls')),

    # Client URLs
    path('client/contact/', include('client.contact.urls')),
    path('client/payment/', include('client.payment.urls')),
    path('client/register/', include('client.register.urls')),
    path('client/schedule/', include('client.schedule.urls')),

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
