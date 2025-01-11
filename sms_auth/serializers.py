from rest_framework import serializers

class SMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=20)

class VerifySMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=20)
    verification_code = serializers.CharField(max_length=20)
