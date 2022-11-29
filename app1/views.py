from django.shortcuts import render

# Create your views here.

def dj(request):
    return render(request,'dj.html')