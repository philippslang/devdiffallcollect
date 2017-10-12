from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework import views
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Result
from .serializers import ResultSerializer


@api_view(['POST'])
def result(request, format=None):
    """
    Post a devDiffAll.py result.
    """
    if 0: # shorthand to delete all previous data
        Result.objects.all().delete()
    if 0: # delete entries with no duration data
        delset = Result.objects.all()
        for obj in delset:
            if obj.duration_ix == 'NA':
                obj.delete()
    serializer = ResultSerializer(data=request.data)
    if serializer.is_valid():   
        serializer.save()       
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def results_v0(request, format=None):
    """
    Lists 50 most recently posted devDiffAll.py results.
    """
    allresults = Result.objects.all().order_by('-posted')[:50]
    serializer = ResultSerializer(allresults, many=True)
    return Response(serializer.data)

    
class ResultsView(viewsets.ModelViewSet):
    """
    Access submitted results.
    """
    #authentication_classes = (authentication.TokenAuthentication,)
    #permission_classes = (permissions.AllowAny,)
    queryset = Result.objects.all().order_by('-posted')
    serializer_class = ResultSerializer
