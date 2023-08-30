
from django.contrib import admin
from django.urls import path
from invista_me import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.investimentos),
    path('contactos/',views.pagina_de_contacto, name = 'contactos'),
    path('minha/historia/',views.minha_historia),
    path('novo_investimento',views.novo_investimento, name = 'novo_investimento'),
    path('investimento_registrado',views.investimento_registrado,name = 'investimento_registrado'),
]
