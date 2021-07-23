from django.urls import path
from .views import PeopleDetailView, FilmoListView, MovieDetailPeopleListView

urlpatterns = [
    path('detail/<pk>', PeopleDetailView.as_view(), name='people_detail'), # 단일 영화인 간단 정보
    path('filmo/<pk>', FilmoListView.as_view(), name='filmo_list'), # 단일 영화인의 필모 정보영화
    path('list/<pk>', MovieDetailPeopleListView.as_view(), name='movie_detail_people_list'), # 영화 디테일 페이지 들어 갔을 때 나오는 영화인 리스트
]