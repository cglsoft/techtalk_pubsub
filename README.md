### TechTalk - Maio/ Junho /2020

 Projeto para demonstracao das funcionalidade do PUBSUB com Python
 Autor : Claudio Lisboa
 Referencias: https://cloud.google.com/pubsub/docs


#### Projeto PYTHON para demonstração de consumo API Google PubSub

Preparacao do Ambiente GCP Desenvolvimento.
Versao 1.00- 30/05/2020
Google Cloub Pub/Sub Pyhton configuracao de ambiente

***
##### Preparando o ambiente para execucao local.
Referência: https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu

##### Add the Cloud SDK distribution URI as a package source
```bash {cmd}
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
```

##### Import the Google Cloud Platform public key
```bash {cmd}
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
```

##### Update the package list and install the Cloud SDK
```bash {cmd}
sudo apt-get update && sudo apt-get install google-cloud-sdk
```

##### Inicializar o SDK
Use o comando  abaixo  para executar várias tarefas comuns de configuração do SDK. entre elas:
autorizar as ferramentas do SDK a acessar o Google Cloud Platform usando as credenciais da sua
conta de usuário e definir a configuração padrão do SDK.

Para iniciar o SDK:

```bash {cmd}
gcloud init
```

##### Definindo o projeto DEFAULT
```bash {cmd}
gcloud config set project projeto-pubsub
``` 

Exportar a chave de servico para funcionar as autenticacoes: https://cloud.google.com/docs/authentication/getting-started

##### Este passo é importante para configurar o local da chave de segurança IAM para autenticação das ferramentas do google
```bash {cmd}
export GOOGLE_APPLICATION_CREDENTIALS="/home/lisboa/cglsoft/gcp_Carrefour/key.json"
```

#### PYTHON INSTALL UBUNTU CONFIGURATION

##### Step 1: Update your repositories
```bash {cmd}
sudo apt-get update
```

##### Step 2: Install pip for Python 3
```bash {cmd}
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo apt install python3-pip
```

##### Step 3: Use pip to install virtualenv
```bash {cmd}
sudo pip3 install virtualenv
```

##### Step 4: Launch your Python 3 virtual environment, here the name of my virtual environment will be env3
```bash {cmd}
virtualenv -p python3 env3
```

##### Step 5: Activate your new Python 3 environment. There are two ways to do this
```bash {cmd}
. env3/bin/activate #####  or source env3/bin/activate which does exactly the same thing
```

##### you can make sure you are now working with Python 3
```bash {cmd}
python -- version
```

##### this command will show you what is going on: the python executable you are using is now located inside your virtualenv repository
```bash {cmd}
which python
```

##### Step 6: code your stuff
##### Step 7: done? leave the virtual environment

___
##### Acessar o Terminal e preparar o ambiente para testar a solucao:

###### Criar diretorio para simular os testes:

Criacao do ambiente virtual PYTHON
```bash {cmd}
python -m virtualenv env
```

Ativar o ambiente virtual
```bash {cmd}
source env/bin/activate
```

Instalacao biblioteca Pub/Sub PYTHON
```bash {cmd}
pip install --upgrade google-cloud-pubsub
```

Comandos SHELL para verificar os tópicos
```bash {cmd}
gcloud pubsub topics create my-topic
gcloud pubsub subscriptions create my-sub --topic my-topic
```

Comandos pubsub Listar topicos e subscriptions
```bash {cmd}
gcloud pubsub topics list
gcloud pubsub subscriptions list
gcloud info
```

##### Execucao em dois terminais diferentes para validar a solução de publicação e consumo de informações:

##### TOPIC - Testes
Check com os programas Publisher e Subscriber - Python:
```bash {cmd}
python publisher3.py projeto-pubsub my-topic
```

##### SUBSCRIBER - Testes
```bash {cmd}
python subscriber.py projeto-pubsub my-topic
```

---
##### Comandos gerais PubSub

Comandos terminal para PUB/SUB para apagar  Subscriptions e TOPIC
```bash {cmd}
gcloud pubsub subscriptions delete my-sub
gcloud pubsub topics delete my-topic
```


### Author

**Claudio Lisboa**

* [github/cglsoft](https://github.com/cglsoft)

### License

Copyright © 2008-2020, [CGLSOFT Desenvolvimento](https://github.com/cglsoft).
Released under the [MIT License](LICENSE).

***