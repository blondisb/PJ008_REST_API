from rest_framework import serializers
from .models import MO_projects

class SE_project(serializers.ModelSerializer):
    class Meta:
        model = MO_projects
        fields = ('id', 'title', 'description', 'tech', 'date_created')
        read_only_fields = ('date_created',)
