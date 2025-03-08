from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include  # Include function needs to be imported

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('api/', include('study.urls')),  # Include the study planner app's URLs under /api/
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
