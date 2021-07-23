from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import MovieListSerializer, MovieInfoSerializer
from .pagination import MovieListPagination
from .models import Movie
from collections import defaultdict


SEARCH_FIELD = ['movienm', 'prdtstatnm', 'genrealt'] # 개봉상태, 장르, 영화 이름

class MovieShowingView(ListAPIView):
    serializer_class = MovieListSerializer
    pagination_class = MovieListPagination

    def get_queryset(self):
        self.params = defaultdict(list, self.request.query_params)
        return Movie.objects.filter(prdtstatnm='개봉')


class MovieRankingView(ListAPIView):
    serializer_class = MovieListSerializer
    pagination_class = MovieListPagination

    def get_queryset(self):
        self.params = defaultdict(list, self.request.query_params)
        gen_list = self.params['genre']

        if gen_list :
            ret = Movie.objects.filter(genre__genrealt__in=gen_list)
        else :
            ret = Movie.objects.all()

        return ret


class MovieSearchingView(ListAPIView):
    serializer_class = MovieListSerializer
    pagination_class = MovieListPagination

    def get_queryset(self):
        self.params = defaultdict(list, self.request.query_params)
        print(self.params)
        target = self.params['search_info'][0]
        ret = Movie.objects.filter(movienm__startswith=target)
        return ret


class MovieDetailView(RetrieveAPIView):
    serializer_class = MovieInfoSerializer
    queryset = Movie.objects.all()



