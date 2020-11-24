# Eventex
Sistema de eventos encomendado pela morena

## como desenvolver
1. Clone o repositorio
1. Crie um virtual env com python
1. Ative seu virtual env
1. Instale as dependencias
1. Configure a instancia com  .env
1. Execute os testes

```console
git clone git@github.com:FelipeSBarros/wttd_eventex.git wttd
cd wdtt
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-semple .env
python manage test 
```

## Como fazer deploy

1. crie uma instancia no heroku
1. envie aas configurações para o heroku
1. defina secretkey para a instancia
1. defina DEBUG=False
1. configura o serviço de e-mail
1. envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`ýthon contrib/secret_gen.py`
heroku config:set DEBUG=False
# configure email
gut push heroku master --force
```
