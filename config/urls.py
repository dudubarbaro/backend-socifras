from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from socifras.views import MusicaViewSet, ArtistaViewSet, GeneroViewSet, VideoAulasViewSet

router = DefaultRouter()
router.register(r"musicas", MusicaViewSet)
router.register(r"artistas", ArtistaViewSet)
router.register(r"generos", GeneroViewSet)
router.register(r"videoaulas", VideoAulasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
