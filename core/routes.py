from rest_framework.routers import DefaultRouter

from .views import users_view

router = DefaultRouter()

router.register(r'users', users_view.UserViewSet, basename='users')
