from django.shortcuts import render

def home(request):
    # Logic to retrieve data and render it in the template goes here
    context = {
        'title': 'Welcome to My Website',
        'message': 'Hello, world!'
    }
    return render(request, 'home.html', context)
