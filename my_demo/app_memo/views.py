from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm

#create your views here
from .models import *
from .forms import createUserForm


def register(request):
    template = loader.get_template('Register.html')
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm()
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context,request))

def login(request):
    template = loader.get_template('login.html')
    
    context = {

    }
    return HttpResponse(template.render(context))

def index(request):
    template = loader.get_template('testing.html')
    return HttpResponse(template.render())
