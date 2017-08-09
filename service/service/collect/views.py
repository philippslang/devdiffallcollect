from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Result
from .serializers import ResultSerializer


@api_view(['POST'])
def result(request, format=None):
    """
    Post a devDiffAll.py result.
    """
    serializer = ResultSerializer(data=request.data)
    if serializer.is_valid():        
        serializer.save()       
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def results(request, format=None):
    """
    List all posted devDiffAll.py results.
    """
    allresults = Result.objects.all()
    serializer = ResultSerializer(allresults, many=True)
    return Response(serializer.data)

