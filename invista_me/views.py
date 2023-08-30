from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Investimento
from .forms import InvestimentoForm

def pagina_inicial(request):
	return HttpResponse('Pronto para investir')

def pagina_de_contacto(request):
	return HttpResponse('Esta e a pagina de contacto')

def minha_historia(request):
	pessoa = {
		'nome':'HP',
		'idade':90,
		'hobby':'rest'
	}
	return render(request,'investimentos/minha_historia.html',pessoa)

def investimento_registrado(request):
	investimento = {
		'tipo_investimento':request.POST.get('TipoInvestimento')
	}
	return render(request,'investimentos/investimento_registrado.html',investimento)

def investimentos(request):
	dados = {
		'dados':Investimento.objects.all()
	}
	return render(request,'investimentos/investimentos.html',context = dados)

def detalhe(request,id_investimento):
	dados = {
		'dados':Investimento.objects.get(pk=id_investimento)
	}
	return render(request,'investimentos/detalhe.html',context=dados)

def criar(request):
	investimento_form = InvestimentoForm()
	formulario = {
		'formulario':investimento_form
	}
	return render(request,'investimentos/novo_investimento.html',context = formulario)



























