from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
from .models import TextBot
import os


# Create your views here.
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def home(request):
    return render(request, 'home.html')

def chatroom(request):
    return render(request, 'chatroom.html')

def textbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('userInput')  
        completion = client.chat.completions.create(model='gpt-4o', messages=[{'role': 'user', 'content': user_input}])
        message = completion.choices[0].message
        return render(request, 'chatpage.html', context={'message': message})

    

