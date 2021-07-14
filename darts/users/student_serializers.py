from django.db.models import Sum
from rest_framework import serializers

from marks.models import Marks
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    """
    Marks Serializer
    """
    total_marks = serializers.SerializerMethodField(read_only=True)

    def get_total_marks(self, obj):
        """ Return total marks for each student """
        return Marks.objects.filter(student=obj).aggregate(Sum('marks')).get("marks__sum")

    class Meta:
        model = Student
        fields = ("id", "user", "standard", "total_marks")
