from rest_framework.routers import DefaultRouter

from .views import BarrelSetViewSet, BarrelViewSet

router = DefaultRouter()
router.register(r'barrel_sets', BarrelSetViewSet, basename='barrel_sets')
router.register(r'barrels', BarrelViewSet, basename='barrels')
urlpatterns = router.urls
