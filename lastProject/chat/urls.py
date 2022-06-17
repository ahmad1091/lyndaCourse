from django.urls import path
from chat.views import RoomList,MessageList


urlpatterns = [
    path('', RoomList.as_view()),    
    path('<int:id>/message/', MessageList.as_view()),
    
]