from django.shortcuts import render

from app.forms import *
from django.http import HttpResponse

# Create your views here.
def registration(request):
    ERFO=RegistrationForm()
    d={'ERFO':ERFO}
    if(request.method=='POST'):
        RDFO=RegistrationForm(request.POST)
        if(RDFO.is_valid()):
            return HttpResponse(str(RDFO.cleaned_data))
    return render(request,'registration.html',d)
