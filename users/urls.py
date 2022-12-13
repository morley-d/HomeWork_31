from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token


from users import views

urlpatterns = [
    path('', views.UserView.as_view()),
    path('<int:pk>/', views.UserDetailView.as_view()),
    path('create/', views.UserCreateView.as_view()),
    path('<int:pk>/update/', views.UserUpdateView.as_view()),
    path('<int:pk>/delete/', views.UserDeleteView.as_view()),
    path('login/', obtain_auth_token),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

