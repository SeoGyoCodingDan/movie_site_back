from rest_framework import serializers
from .models import People

class PersonInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ['peoplecd', 'peoplenm', 'sex', 'reprolenm']


class FilmoListSerializer(serializers.Serializer):
    posterurl = serializers.CharField(max_length=255)
    movienm = serializers.CharField(max_length=255)
    moviepartnm = serializers.CharField(max_length=100)