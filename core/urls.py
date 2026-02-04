from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.views import (
    home, JobListAPI, JobCreateAPI,
    ApplicationListAPI, ApplicationCreateAPI,
    RegisterView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Day 3 Task URL (Root URL)
    path('', home, name='home'),

    # Day 5/7 API URLs
    path('api/jobs/', JobListAPI.as_view(), name='job-list'),
    path('api/jobs/create/', JobCreateAPI.as_view(), name='job-create'),
    path('api/applications/', ApplicationListAPI.as_view(), name='application-list'),
    path('api/applications/create/',
         ApplicationCreateAPI.as_view(), name='application-create'),
    path('api/signup/', RegisterView.as_view(), name='auth_register'),

    # --- Day 9 JWT Login URLs (Ee rande ennam koodi add cheyyu) ---
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
