from operator import length_hint
from xml.dom.minidom import CharacterData
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def password(request):
    characters = list('qwertyuioplkjhgfdsazxcvbnm')
    generated_password = ''
    
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        characters.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
    
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()/')
        
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    
    for x in range(length):
         generated_password += random.choice(characters)
         
    return render(request, 'password.html', {'password': generated_password})
    