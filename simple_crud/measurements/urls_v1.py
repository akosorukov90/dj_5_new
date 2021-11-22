from rest_framework.routers import DefaultRouter
from .api_views_v1 import ProjectViewSet, MeasurementViewSet

router = DefaultRouter()
router.register(r'project', ProjectViewSet)
router.register(r'measurement', MeasurementViewSet)

urlpatterns = router.urls
