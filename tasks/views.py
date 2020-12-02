from django.http import HttpResponse, Http404, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from tasks.serializer import TaskSerializer
from tasks.models import Task


def index(_request):
    return HttpResponse("Hello, world. You're at the tasks index.")


@api_view(["GET"])
def get_all_tasks(_request):
    # pylint: disable=no-member
    data = TaskSerializer(Task.objects.all(), many=True)
    return JsonResponse(data.data, safe=False)


@api_view(["GET"])
def get_task(_request, title):
    # pylint: disable=no-member
    try:
        data = TaskSerializer(Task.objects.filter(title=title), many=True)
        return JsonResponse(data.data, safe=False)
    except Task.DoesNotExist:
        return Http404("Task not found")


@api_view(["POST"])
def create_task(request):
    data = JSONParser().parse(request)
    serializer = TaskSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@api_view(["DELETE"])
def delete_task(_request, title):
    # pylint: disable=no-member
    try:
        Task.objects.get(title=title).delete()
    except Task.DoesNotExist:
        return Http404("Task not found")

    return HttpResponse("Task deleted")


@api_view(["DELETE"])
def delete_all_tasks(_request):
    # pylint: disable=no-member
    Task.objects.all().delete()
    return HttpResponse("All tasks deleted")
