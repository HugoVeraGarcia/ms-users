from django.urls import path
from .views import auth_view
from .views import status_view
from .routes import router

urlpatterns = [
   path('status', status_view.StatusView.as_view()),
   path('register', auth_view.RegisterView.as_view()),
   path('login', auth_view.LoginView.as_view()),
   path('user', auth_view.UserView.as_view()),
   path('logout', auth_view.LogoutView.as_view()),
]

urlpatterns += router.urls