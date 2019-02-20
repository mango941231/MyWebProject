from .models import Goods
from .serializer import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics


class GoodsPagination(PageNumberPagination):
    """
    配置分页规则
    """
    page_size = 1
    page_query_param = 'p'
    page_size_query_param = 'page_size'
    max_page_size = 1000

class GoodsListViewSet(generics.ListAPIView):

    queryset = Goods.objects.get_queryset().order_by('id')
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
