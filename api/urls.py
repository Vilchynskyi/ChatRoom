from django.urls import path
from .views import MessagesAPIView, MessageDetailAPIView


app_name = 'api'

urlpatterns = [
    path('messages/list/', MessagesAPIView.as_view(), name='message_list'),
    path('messages/single/<pk>', MessageDetailAPIView.as_view(), name='single_message')
]
