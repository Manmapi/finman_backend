from rest_framework import serializers
from ..models import WatchHealthData


class WatchHealthDataSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = WatchHealthData
        fields = ['user', 'watch_id', 'time', 'value', 'type']




