from django.shortcuts import render

# Create your views here.
def servicesLender(request):
    return render(request, 'services/index.html', {})

def servicesOwner(request):
    return render(request, 'services/index1.html', {})

def servicesBuilding(request):
    return render(request, 'services/index2.html', {})

def servicesLitigation(request):
    return render(request, 'services/index3.html', {})