from django.contrib import admin
from django.urls import path, include
from users.views import CreateUserView, CustomAuthToken, UserDetailView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', CreateUserView.as_view(), name='signup'),
    path('api/login/', CustomAuthToken.as_view(), name='login'),
    path('api/user/', UserDetailView.as_view(), name='user-detail'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]