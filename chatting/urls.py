from django.urls import path
from chatting import views

urlpatterns = [
    path('', views.chat_room),  #
    path('chat/', views.chat)
]