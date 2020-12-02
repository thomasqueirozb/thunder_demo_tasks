from rest_framework.serializers import ModelSerializer

from .models import Task

# pylint: disable=too-few-public-methods
class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ("title", "pub_date", "description")
