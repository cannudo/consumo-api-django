# Tutorial: consumindo uma API com Django

Olá, pessoal. Como vão? O objetivo deste tutorial é compartilhar o conhecimento obtido por mim após dois dias de pesquisa sobre como consumir uma API usando Django. Precisei disso para o meu projeto integrador na faculdade.

## Pré-requisitos

Para seguir com este tutorial, é recomendável que você tenha noções básicas sobre:
- Django 2.0
- Python 3.6 e suas estruturas de dados
- HTML
- APIs REST
- Manipulação de JSONs

## Funcionamento
Para construir o conhecimento de forma mais concisa, você poderá acompanhar a explicação deste arquivo e todo o código gerado estará disponível em [codigo](/codigo)

---

# Tutorial

## API: IBGE
Para iniciar minhas pesquisas, precisei escolher uma API existente que me retornasse dados sem necessidade de autenticação. O IBGE, em seu [site de APIs](https://servicodados.ibge.gov.br/api/docs), disponibiliza mais ou menos 12 serviços do tipo. Eu escolhi a API de **localidades**, que é referente às divisões político-administrativas do Brasil. Leia a documentação referente: [API de localidades](https://servicodados.ibge.gov.br/api/docs/localidades?versao=1)

### Escolha dos recursos
Depois de ler a documentação, escolhi o recurso que me retornava uma lista de municípios de determinada unidade federativa:

![barra lateral da API do IBGE](/image.png)

Mas para isso, precisava antes ter em mãos o id da unidade federativa. Em [outra seção do site](https://servicodados.ibge.gov.br/api/docs/localidades?versao=1#api-UFs-estadosGet), consegui o id 24, referente a unidade federativa do **Rio Grande do Norte**, inspecionando o [JSON](https://servicodados.ibge.gov.br/api/v1/localidades/estados/) que me foi retornado no navegador:

![JSON visto do navegador Firefox](/image2.png)

Então, de posse do ID, acessei: https://servicodados.ibge.gov.br/api/v1/localidades/estados/24/municipios

Agora, com esse endereço me retornando informações referentes aos municípios, suas micro e mesorregiões em formato JSON, estava preparado para o código.

## Projeto Django
Para consumir dados dessa API, precisaremos apenas das views e dos templates no Django. Inicializaremos um projeto Django:

![Terminal após o início do projeto Django](/image3.png)

**Observação:** após iniciar o projeto, mudei o nome da pasta para _codigo_

E depois, uma aplicação chamada _ibge_:

![Terminal após o inicio da aplicação](/image4.png)

### Configuração básica
Na pasta da aplicação, criei um diretório chamado _templates_, bem como os arquivos _index.html_ dentro dele e _urls.py_, externamente:

![printscreen da árvore de diretórios](/image6.png)

Também adicionei a aplicação recém-criada ao projeto:

![printscreen do arquivo de configuração do projeto](/image5.png)

Após isso, configurei as rotas:

[em cima, arquivo de urls do projeto, em baixo, da aplicação](/image7.png)

Depois de fazer essas configurações básicas do Django, está na hora de views e templates
