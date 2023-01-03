from .models import MO_projects
from .serializers import SE_project
from rest_framework import viewsets, permissions

class AP_ProjectViewSet(viewsets.ModelViewSet):
    queryset = MO_projects.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SE_project