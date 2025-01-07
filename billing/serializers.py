from rest_framework.serializers import ModelSerializer
from .models import Bill

class billSer(ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"