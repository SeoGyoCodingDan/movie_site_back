from rest_framework.pagination import PageNumberPagination

class MovieListPagination(PageNumberPagination):
    page = 1
    page_size = 10
    max_page_size = 100 # 이 숫자 넘어도 에러 없이 100개만 반환
    page_query_param = 'page'
    page_size_query_param = 'page_size'
