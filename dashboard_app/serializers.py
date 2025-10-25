from rest_framework import serializers
from .models import LogAnalytics

class LogAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogAnalytics
        fields = "__all__"
