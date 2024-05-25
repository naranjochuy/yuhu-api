from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from utils.pagination import ResultSetPagination
from .models import Task
from .serializers import TaskSerializer
from .tasks import send_email_task


class TaskViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    http_method_names = ["get", "post", "put", "delete"]
    ordering_fields = ["title", "email", "expiration_date"]
    pagination_class = ResultSetPagination
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    search_fields = ["title", "description", "email"]
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save()
        send_email_task.delay()

    def perform_update(self, serializer):
        serializer.save()
        send_email_task.delay()
