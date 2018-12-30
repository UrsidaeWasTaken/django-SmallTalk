from django.urls import path
from chat import views

urlpatterns = [
    # /<room_id>/
    path('<room_id>', views.room),

    # /<room_id>/messages
    path('<room_id>/messages', views.messages)
]
