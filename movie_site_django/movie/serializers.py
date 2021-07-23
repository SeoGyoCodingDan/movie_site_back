from rest_framework import serializers
from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['movienm', 'posterurl']


class MovieInfoSerializer(serializers.ModelSerializer):

    class Meta :
        model = Movie
        fields = ['movienm', 'prdtyear', 'opendt', 'prdtstatnm', 'repnationnm', 'posterurl',]