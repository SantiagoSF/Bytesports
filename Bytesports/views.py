from django.shortcuts import render
#importamos nuestro form para usarlo
from Bytesports.models import Match
from Bytesports.forms import MatchForm
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    retas = Match.objects.all()
    return render(request, 'dashboard.html', locals())

def create_match(request):
	"""Regresa el formulario MatchForm al template createMatch"""
	#creamos la instancia del formulario
	form = MatchForm()
	return render(request, 'createMatch.html', locals())

def save_match(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MatchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/home/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MatchForm()

    return render(request, 'createMatch.html', {'form': form})

def view_match(request):
	return render(request, 'match-info.html')
