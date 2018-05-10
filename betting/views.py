from django.shortcuts import render

# Create your views here.
def added_game(request):
    return render(request, 'betting/test.html')
