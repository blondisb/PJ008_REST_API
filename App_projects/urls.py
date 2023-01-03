# from django.urls import path
from rest_framework import routers
from .api import AP_ProjectViewSet

router = routers.DefaultRouter()
router.register('api/projects', AP_ProjectViewSet, 'projects')

urlpatterns = router.urls