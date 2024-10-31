from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

from .models import TextBot

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Create your views here.
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def question(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    message = response.text
    return message

def home(request):
    return render(request, 'home.html')

def chatroom(request):
    return render(request, 'chatroom.html')

def textbot(request):
    convo = TextBot.objects.filter(user=request.user)

    if request.method == 'POST':
        user_input = request.POST.get('userInput')
        answer = question(user_input)

        chat = TextBot(user=request.user, message=user_input, response=answer, time=timezone.now)
        chat.save()

        return JsonResponse({'message': user_input, 'response': answer})

    return render(request, 'chatroom.html', context={'convo': convo})

    

