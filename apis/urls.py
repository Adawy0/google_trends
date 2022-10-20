
from django.urls import path, include

from .views import historical_interest, interest_by_region, read_data
urlpatterns = [
    path('historical-interest/', historical_interest),
    path('interest-by-region/', interest_by_region),
    path('read-data/', read_data),
]