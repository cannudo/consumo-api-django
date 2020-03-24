# Tutorial: consumindo uma API com Django

Olá, pessoal. Como vão? O objetivo deste tutorial é compartilhar o conhecimento obtido por mim após dois dias de pesquisa sobre como consumir uma API usando Django. Precisei disso para o meu projeto integrador na faculdade.

## Pré-requisitos

Para seguir com este tutorial, é recomendável que você tenha noções básicas sobre:
- Django 2.0
- Python 3.6 e suas estruturas de dados
- HTML
- APIs REST

## Funcionamento
Para construir o conhecimento de forma mais concisa, você poderá acompanhar a explicação deste arquivo e todo o código gerado estará disponível em [codigo](/codigo)

---

# Tutorial

## API: IBGE
Para iniciar minhas pesquisas, precisei escolher uma API existente que me retornasse dados sem necessidade de autenticação. O IBGE, em seu [site de APIs](https://servicodados.ibge.gov.br/api/docs), disponibiliza mais ou menos 12 serviços do tipo. Eu escolhi a API de **localidades**, que é referente às divisões político-administrativas do Brasil. Leia a documentação referente: [API de localidades](https://servicodados.ibge.gov.br/api/docs/localidades?versao=1)
