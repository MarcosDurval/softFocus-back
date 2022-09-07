# Teste SoftFocus Full stack

Clicando [aqui](https://github.com/MarcosDurval/softFocus-front) você encontra o front end


## Construção

A aplicação foi construida usando Django Rest framework

Para calcular a distância com base na longitude e latitude que se obtém atrás da Fórmula de [haversine](https://pt.wikipedia.org/wiki/F%C3%B3rmula_de_haversine) foi utilizado a biblioteca [haversine](https://pypi.org/project/haversine/) 


## Como executar localmente  

clone o Projeto:
```
git clone git@github.com:MarcosDurval/softFocus-back.git
```

entre no diretório:
```
cd softFocus-back
```

#### Renomeei o arquivo .env.example que está no diretório softfocus para .env

Criando um .venv

```
python3 -m venv .venv
```
Ativando o ambiente virtual:

```
source .venv/bin/activate
```
Instalando as dependências:
```
python3 -m pip install requirements.txt
```

Executando makemigrations:
```
python3 manage.py  makemigrations
```

Executando migrate:

```
python3 manage.py  migrate
```
Executando o app:

```
python3 manage.py  runserver
```

