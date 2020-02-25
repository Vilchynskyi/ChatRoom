from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Message
from .serializers import MessageSerializer


class MessagesPagination(PageNumberPagination):
    page_size = 10
    invalid_page_message = 'Page not found'
    # page_size_query_param = 'page_size'


class MessagesAPIView(ListAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ('author',)
    search_fields = ('author',)
    ordering_filters = ('id', 'create_date', 'update_date',)
    pagination_class = MessagesPagination

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


class MessageDetailAPIView(APIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get(self, request, pk):
        message_qs = Message.objects.filter(id=pk)
        serializer = MessageSerializer(message_qs, many=True)
        return Response(serializer.data)
