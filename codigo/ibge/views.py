from django.shortcuts import render
import requests # faz requisições HTTP

def index(request):
    api = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/24/municipios"
    requisicao = requests.get(api)
    lista = requisicao.json()
    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    contexto = {
        "municipios": dicionario
    }

    return render(request, "aplicacao/index.html", contexto)
