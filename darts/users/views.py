""" Viewsets for Student """

from rest_framework.viewsets import ModelViewSet
from .student_serializers import StudentSerializer

from .models import Student

class StudentViewSet(ModelViewSet):
    """
    Student related API
    """
    serializer_class = StudentSerializer
    # filterset_class = PartFilterSet
    ordering = ("-created_at",)

    def get_queryset(self):
        return Student.objects.all()
