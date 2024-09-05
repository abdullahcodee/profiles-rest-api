from rest_framework import serializers

class HelloSerialzer(serializers.Serializer):
    name = serializers.CharField(max_length = 10)