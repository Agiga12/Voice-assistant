from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
path('start-voice-assistant/', views.start_voice_assistant_view, name='start-voice-assistant'),
    # Добавьте другие маршруты здесь, если они у вас есть
]