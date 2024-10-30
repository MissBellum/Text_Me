from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
from dotenv import load_dotenv
# from .models import TextBot
import os

load_dotenv()

# Create your views here.
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)

def home(request):
    return render(request, 'home.html')

def chatroom(request):
    return render(request, 'chatroom.html')

# def textbot(request):
#     if request.method == 'POST':
#         user_input = request.POST.get('userInput')  
#         completion = client.chat.completions.create(model='gpt-4o', messages=[{'role': 'user', 'content': user_input}])
#         message = completion.choices[0].message
#         return render(request, 'chatpage.html', context={'message': message})

    

