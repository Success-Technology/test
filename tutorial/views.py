from django.shortcuts import render

# Create your views here.
def launch_tutorial(request):
    return render(request,"founder.html")