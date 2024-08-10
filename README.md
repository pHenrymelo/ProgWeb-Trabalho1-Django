# Agenda de Atividades - Trabalho Programação Web

## Requerimentos

- Python 3

## Configurando o ambiente

Instale as dependências do Python com o seguinte comando:

    pip install -r requirements.txt


Configuração das Variáveis de Ambiente

Ajuste os valores default do DATABASE no arquivo settings.py do app base do projeto Activity_schedule.


    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{nome_do_banco_de_dados}',
        'USER': '{usuario_do_banco_de_dados}',
        'PASSWORD': '{senha_do_banco_de_dados}',
        'HOST': '{endereco_do_banco_de_dados}',
        'PORT': {porta_do_banco_de_dados}
      }
    }

Substitua os valores entre chaves pelos valores correspondentes do seu ambiente.

## Uso

Ative o ambiente virtual (caso esteja utilizando):

    source path/to/venv/bin/activate  # Linux/macOS
    path\to\venv\Scripts\activate      # Windows

Se estiver rodando a primeira vez, faça as migrações dos modelos:

    python manage.py makemigrations
    python manage.py migrate

E por fim, execute o servidor Django:

    python manage.py runserver
