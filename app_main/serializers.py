from rest_framework import serializers
from .models import Values


class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Values
        fields = "__all__"
