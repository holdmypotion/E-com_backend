from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, \
                                            TokenRefreshView

from user.api import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
