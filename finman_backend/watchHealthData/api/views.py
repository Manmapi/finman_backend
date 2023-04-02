import datetime
from rest_framework import status

from rest_framework import generics
from rest_framework import permissions
from django.utils import timezone
from .serializers import WatchHealthDataSerializer
from ..models import WatchHealthData
from rest_framework.decorators import api_view, permission_classes
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response


# Create your views here.


class WatchHealthDataList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = WatchHealthData.objects.all()
    serializer_class = WatchHealthDataSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(WatchHealthDataList, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        return WatchHealthData.objects.filter(user=user)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_watch_data_in_range(request):
    params = request.GET
    user = request.user
    day_limit = int(params.get('duration', '30'))
    type_data = params.get('type', 'all')

    now = timezone.now()
    before_time = now - datetime.timedelta(days=day_limit)
    try:
        if type_data == 'all':
            data = WatchHealthData.objects.filter(time__range=[before_time, now], user=user)
        else:
            data = WatchHealthData.objects.filter(time__range=[before_time, now], type=type_data, user=user)
        body_response = WatchHealthDataSerializer(data, many=True)
        return Response(body_response.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response([], status=status.HTTP_404_NOT_FOUND)
