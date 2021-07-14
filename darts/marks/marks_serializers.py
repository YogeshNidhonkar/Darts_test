from rest_framework import serializers
from .models import Marks


class MarksSerializer(serializers.ModelSerializer):
    """
    Marks Serializer
    """

    class Meta:
        model = Marks
        fields = ("id", "student", "subject", "marks")
