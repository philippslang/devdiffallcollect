from .models import Result
from rest_framework import serializers


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('posted', 'origin', 'platform', 'cl', 'tests', 'status', 'instrumentation', 
          'configuration', 'duration_ix', 'duration_ecl2ix', 'num_processes_ix', 'num_threads_ix',
          'test_suite')

