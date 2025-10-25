from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LogAnalytics
from .serializers import LogAnalyticsSerializer
from kafka import KafkaConsumer
import json

@api_view(['GET'])
def get_dashboard(request):
    # logs = LogAnalytics.objects.all().order_by('-created_at')
    # serializer = LogAnalyticsSerializer(logs, many=True)
    # return Response(serializer.data)



    print("Received log data:")
    consumer = KafkaConsumer(
        'logs.uploaded',
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    for message in consumer:
        data = message.value
        print(f"Received log data: {data}")
    
    return Response({
            "message": "Working"
        })
