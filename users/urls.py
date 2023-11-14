from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import UserListView, UserRetrieveView, UserCreateView, UserUpdateView, UserDestroyView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('list/', UserListView.as_view(), name='list'),
    path('<int:pk>', UserRetrieveView.as_view(), name='retrieve'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', UserDestroyView.as_view(), name='delete'),
]
