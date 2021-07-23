from django.urls import path
from .views import (MovieShowingView, MovieRankingView, MovieSearchingView, MovieDetailView )

urlpatterns = [
    path('showing', MovieShowingView.as_view(), name='movie_showing'), # 상영 중인 영화 보여주기
    path('ranking/', MovieRankingView.as_view(), name='movie_ranking'), # 영화 장르 별 랭킹 순위로 보옂귀
    path('searching/', MovieSearchingView.as_view(), name='movie_searching'), # 영화 검색
    path('detail/<pk>', MovieDetailView.as_view(), name='movie_detail'), # detail
]