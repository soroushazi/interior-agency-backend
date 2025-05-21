from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from users.auth import EmailTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


urlpatterns = [
    path('api/users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login: get access & refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refresh access token
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

