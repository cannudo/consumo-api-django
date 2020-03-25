# Tutorial: consumindo uma API com Django

O objetivo deste tutorial é compartilhar o conhecimento obtido por mim após dois dias de pesquisa sobre como consumir uma API usando Django. Precisei disso para o meu projeto integrador na faculdade e estava batendo cabeça porque, às vezes, um arquivo JSON é muito grande e é difícil de manipulá-lo, já que Python não oferece isso de forma nativa. Depois de muita pesquisa, finalmente consegui construir um front-end, ainda que arcaico, mas consumindo de uma API em produção.

## O que isto não é
Este tutorial não pretende ensinar, completamente
- **Django**: a equipe do Django tem uma documentação ótima! Você pode acessá-la [clicando aqui](https://www.djangoproject.com/). Pretendo fazer um outro projeto compartilhando meu conhecimento sobre Django também, mas não é o caso deste repositório
- **Python**: na [W3Schools](https://www.w3schools.com) tem um [tutorial ótimo](https://www.w3schools.com/python/default.asp) sobre Python
- **HTML**: não vamos usar muitos elementos HTML aqui, mas você também pode acessar um [tutorial completo na W3Schools]
- **APIs REST**: definitivamente, não
- **Manipulação de JSONs**: o que faremos aqui é converter JSON para uma estrutura mais compreensível para o Python. Mas é interessante, se você está querendo se aprofundar em consumo de APIs. A W3Schools tem uma [subseção sobre JSON](https://www.w3schools.com/js/js_json_intro.asp)

É bastante recomendável que você tenha tido um pré-contato com os itens acima, embora, ocasionalmente, alguns desses assuntos possam vir a ser discutidos brevemente em algum momento

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

![em cima, arquivo de urls do projeto, em baixo, da aplicação](/image7.png)

Depois de fazer essas configurações básicas do Django, está na hora de views e templates

## Views do Django
No código das [views](/codigo/ibge/views.py) da aplicação, temos a seguinte ordem:
- Na linha 1, importamos o módulo que vai facilitar o trabalho de encaminhamento dos templates ao usuário
- Na linha 2, importamos o módulo que trabalha com requisições HTTP (talvez você tenha que instalá-lo pelo pip: `pip install requests`)
- Na linha 4, abrimos a função que atenderá ao usuário quando ele digitar a URL [localhost:8000](localhost:8000)
- Na linha 5, colocamos a URL da API anteriormente selecionada
- Na linha 6, acionamos o método `get()` do módulo requests, passando a string `api` como parâmetro
  - A requisição GET viaja até a API
- Na linha 7, pegamos uma lista de retorno de `requisicao`
  - O método `json()` só sera bem sucedido se a string de resposta de `requisicao` se esta for escrita em formato JSON
  - Como isso é uma demonstração, assumiremos que vai dar certo e não trataremos possíveis exceções
- Na linha 8, declaramos um dict vazio
  - `dicionario` vai armazenar os valores do list
  - Template não trabalha com lists, só com dicts
- Na linha 10, estamos preenchendo nosso dict
- Na linha 12, colocamos esse dict em uma variável que será encaminhada para o template
- Na linha 16, a view retorna o template index.html para o usuário e a variável de contexto para o desenvolvedor

## Templates do Django
No [código de template](/codigo/ibge/templates/index.html), fazemos uso de um HTML simples, misturado com alguns padrões da _linguagem de templates Django_
- Na linha 10, fazemos um loop dentro do dicionário que foi passada dentro da variável de contexto na view
  - O dicionário vem carregado de int, str e outros dicts:

  ![printscreen de parte do JSON retornado visto do Firefox](/image8.png)

  - Temos, para cada item do dicionário um id (int), um nome (str) e uma microrregião (dict).
- Com esses dados, podemos mostrar ao usuário:
  - O nome de cada municipio
  - O id de cada municipio
  - O nome de cada microrregião
  - O nome de cada mesorregião
