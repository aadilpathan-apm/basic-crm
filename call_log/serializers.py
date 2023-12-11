from call_log import serializers
from .models import CallLog

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallLog
        fields = '__all__'