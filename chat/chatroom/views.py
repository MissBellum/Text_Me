from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        user_input = request.POST.get('userInput')
        answer = question(user_input)

        return render(request, 'chatroom.html', context={'answer': answer})

    

