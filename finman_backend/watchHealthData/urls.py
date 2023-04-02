from django.urls import path

from .api.views import WatchHealthDataList, get_watch_data_in_range

app_name = 'Watch Data'

urlpatterns = [
    path('', WatchHealthDataList.as_view(), name='list_data'),
    path('get_data_in_range', get_watch_data_in_range, name='get_data_in_range')
]
