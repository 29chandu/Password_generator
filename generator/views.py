from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {}
    return render(request, 'generator/home.html', context=context)

def generate_password_view(request):
    print(request)
    context = {'password': 'test_password'}
    return render(request, 'generator/password.html', context=context)