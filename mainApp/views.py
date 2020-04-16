from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainApp/homePage.html')
def ad(request):
    return render(request, 'ad/ad.html')
