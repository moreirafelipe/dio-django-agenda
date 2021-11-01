from django.shortcuts import render
from core.models import Evento
from django.contrib.auth.decorators import login_required
# Create your views here.


# def index(request):
#    return redirect('/agenda')

@login_required(login_url='')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all
    dados = {'eventos': evento}
    return render(request, 'home.html', dados)
