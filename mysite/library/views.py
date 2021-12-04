from django.http.response import FileResponse
from django.shortcuts import render

def home(request):
    return render(request, 'library/home.html')

def image(request):
    return FileResponse(open("C:\\Users\\Shaun\\Downloads\\Bicycle Blue Print Wrap image1.jpg", "rb"))
