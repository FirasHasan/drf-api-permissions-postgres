from rest_framework import serializers
from .models import snacks

class snacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = snacks
        fields = ('id','title','body','author')