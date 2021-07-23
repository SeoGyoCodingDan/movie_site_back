from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import PersonInfoSerializer, FilmoListSerializer
from .models import People, Filmo
from movie.models import Movie

# 영화인 상세 페이지 들어 갔을 때 나오는 단일 영화인 간단 정보
class PeopleDetailView(RetrieveAPIView):
    serializer_class = PersonInfoSerializer
    queryset = People.objects.all()


# 영화인 상세 페이지 들어 갔을 때 나오는 단일 영화인의 필모 정보들
# 영화포스터(model-Movie), 영화이름(Movie), 맡은 배역(Filmo)
class FilmoListView(ListAPIView):
    serializer_class = FilmoListSerializer

    def get_queryset(self):
        people_code = self.kwargs['pk']
        movies = Movie.objects.filter(filmo__peoplecd=people_code).values('posterurl', 'movienm','filmo')
        print(f"movies : {movies}")

        for idx, movie in enumerate(movies):
            filmo = Filmo.objects.get(pk=movie['filmo'])
            movies[idx]['moviepartnm'] = filmo.moviepartnm

        print(f"result : {movies}")

        return movies


# 영화 상세 정보 페이지 들어 갔을 때 나오는 영화인들 목록
class MovieDetailPeopleListView(ListAPIView):
    serializer_class = PersonInfoSerializer

    def get_queryset(self):
        movie_code = self.kwargs['pk']
        people = People.objects.filter(filmo__moviecd=movie_code).values('peoplenm','sex','reprolenm', 'filmo')

        for idx, person in enumerate(people) :
            filmo = Filmo.objects.get(pk=person['filmo'])
            people[idx]['reprolenm'] = filmo.moviepartnm

        return people
