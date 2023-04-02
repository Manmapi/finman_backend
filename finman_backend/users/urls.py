from django.urls import path
from finman_backend.users.api.views import  ListUser
from .api.views import GoogleLogin
app_name = "users"
urlpatterns = [
    path('users', ListUser.as_view(), name='user_list'),
    # path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
]
