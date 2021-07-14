""" Viewsets for Marks """

from rest_framework.viewsets import ModelViewSet
from .marks_serializers import MarksSerializer
from django.db.models import Avg
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Marks

class MarksViewSet(ModelViewSet):
    """
    Part related API
    """
    serializer_class = MarksSerializer
    # filterset_class = PartFilterSet
    ordering = ("-created_at",)

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        if self.request.query_params.get('student'):
            return Marks.objects.filter(student=self.request.query_params.get('student'))
        return Marks.objects.all()

    @action(methods=('get',), detail=False, url_path='average')
    def average(self, request, pk=None):
        """ Return Average of each subject """
        data = {}
        subjects = ["maths", "science", "history", "geography", "english"]
        for subject in subjects:
            data[subject] = Marks.objects.filter(subject=subject).aggregate(Avg('marks')).get("marks__avg")
        return Response(status=status.HTTP_200_OK, data=data)
