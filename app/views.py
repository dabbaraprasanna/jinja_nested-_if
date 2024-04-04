from django.shortcuts import render

# Create your views here.
def nestedif(request):
    d={'a':10,'b':20,'c':23}
    return render(request,'nestedif.html',d)