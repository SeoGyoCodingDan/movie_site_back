from rest_framework import serializers
from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['moviecd', 'movienm', 'posterurl']


class MovieInfoSerializer(serializers.ModelSerializer):

    class Meta :
        model = Movie
        fields = ['moviecd', 'movienm', 'prdtyear', 'opendt', 'prdtstatnm', 'repnationnm', 'posterurl',]