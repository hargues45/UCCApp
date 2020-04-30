from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage/index.html', {})


def thankyou(request):
    return render(request, 'thankyou/thankyou.html', {})