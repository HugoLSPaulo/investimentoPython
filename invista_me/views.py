from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def pagina_inicial(request):
	return HttpResponse('Pronto para investir')

def pagina_de_contacto(request):
	return HttpResponse('Esta e a pagina de contacto')