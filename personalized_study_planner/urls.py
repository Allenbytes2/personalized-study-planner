from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include  # Include function needs to be imported

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API routes from the study app
    path('api/', include('study.urls')),  # Include API-specific routes

    # General routes from the study app
    path('', include('study.urls')),  # Include general routes
]