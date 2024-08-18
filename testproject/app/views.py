from django.shortcuts import render
from django.http import HttpResponse
from app.helpers.voice_assistant import main
def home(request):
    return render(request, 'app/ai_voice_helper.html')

def start_voice_assistant_view(request):
    if request.method == 'POST':
        main()
        return HttpResponse("Voice assistant started successfully!")
    return HttpResponse("This view is meant to be accessed via a POST request only.")
