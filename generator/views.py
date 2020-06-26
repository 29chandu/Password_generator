from django.shortcuts import render

import random

# Create your views here.
def home_view(request):
    context = {}
    return render(request, 'generator/home.html', context=context)

def generate_password_view(request):
    pass_length = int(request.GET.get('length', 0))
    add_letters = request.GET.get('letters')
    add_special = request.GET.get('special')
    add_numbers = request.GET.get('numbers')
    
    # Get upper case and lower case alphabets
    lower_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
    upper_letters = [i.upper() for i in lower_letters]
    all_letters = lower_letters + upper_letters

    special_chars = ['!', '#', '$', '&', '[', ']', '{', '}', '%', '*']
    numbers = list('0123456789')

    total_chars = []
    # if add_letters:
    total_chars.extend(all_letters)
    if add_special:
        total_chars.extend(special_chars)
    if add_numbers:
        total_chars.extend(numbers)

    password = ''
    for i in range(pass_length):
        password += random.choice(total_chars)

    context = {'password': password}
    return render(request, 'generator/password.html', context=context)