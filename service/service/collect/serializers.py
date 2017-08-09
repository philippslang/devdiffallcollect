from .models import Result
from rest_framework import serializers


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('posted', 'origin', 'passed', 'failed', 'gold_diff',)

