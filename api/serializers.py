from rest_framework import serializers, pagination
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    link = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['create_date', 'update_date', ]
