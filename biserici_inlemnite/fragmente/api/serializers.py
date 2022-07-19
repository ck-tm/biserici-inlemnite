from rest_framework import serializers
from wq.db.rest.serializers import ModelSerializer

class GeneralSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
