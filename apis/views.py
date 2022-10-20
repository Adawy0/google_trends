import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from rest_framework import status

from .models import InterestByRegion, HistoricalInterestDataFrame

from .misc import convert_queryset_to_json


from .pytrends import GoogleTrends
# Create your views here.

@api_view(['GET'])
def historical_interest(request):
    if request.method == 'GET':
        try:
            google_trends = GoogleTrends()
            kwlist = request.GET.getlist('kw')
            print(kwlist[0:1])
            if  len(kwlist) == 0:
                raise Exception("historical interest must use one keywork in url queryparams like kw=something")
            google_trends.get_historical_interest(kwlist[0:1])
        except Exception as e:
            print(str(e))
            return Response({"error": str(e)},status= status.HTTP_400_BAD_REQUEST)
    return Response({"message": "data loaded successfully"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def interest_by_region(request):
    if request.method == 'GET':
        try:
            google_trends = GoogleTrends()
            kwlist = request.GET.getlist('kw')
            if  len(kwlist) <= 1:
                raise Exception("interest by region request must use two keyworks in url queryparams like kw=something")
            google_trends.interest_by_region(kwlist[0:2])
        except Exception as e:
            print(str(e))
            return Response({"error": str(e)},status= status.HTTP_400_BAD_REQUEST)
    return Response({"message": "data loaded successfully"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def read_data(request):
    if request.method == 'GET':
        historical_interest_qs =  HistoricalInterestDataFrame.objects.all()
        historical_interest_data = []
        for obj in historical_interest_qs:
            historical_interest_data.append(
                {
                    'date': obj.date,
                    'value': obj.egypt
                }
            )
        return Response(
            {
                "historical_interest": historical_interest_data,
            }, status=status.HTTP_200_OK)
