# Preparacao do Ambiente GCP Desenvolvimento.
# Versao 1.00- 30/05/2020
# Google Cloub Pub/Sub Pyhton configuracao de ambiente
#
#
#  TechTalk DOLPHIN

================================================================================================
Preparando o ambiente para execucao local.
Referência:
https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu

# Add the Cloud SDK distribution URI as a package source
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# Import the Google Cloud Platform public key
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

# Update the package list and install the Cloud SDK
sudo apt-get update && sudo apt-get install google-cloud-sdk


# Inicializar o SDK
# Use o comando gcloud init para executar várias tarefas comuns de configuração do SDK. entre elas:
# autorizar as ferramentas do SDK a acessar o Google Cloud Platform usando as credenciais da sua
# conta de usuário e definir a configuração padrão do SDK.

Para iniciar o SDK:
Execute o seguinte comando em um prompt:

gcloud init

[1] us-east1-b
 [2] us-east1-c
 [3] us-east1-d
 [4] us-east4-c
 [5] us-east4-b
 [6] us-east4-a
 [7] us-central1-c
 [8] us-central1-a
 [9] us-central1-f
 [10] us-central1-b


 =====
 Definindo o projeto DEFAULT
 gcloud config set project projeto-pubsub

# Exportar a chave de servico para funcionar as autenticacoes
# https://cloud.google.com/docs/authentication/getting-started

export GOOGLE_APPLICATION_CREDENTIALS="/home/lisboa/cglsoft/gcp_Carrefour/key.json"


==========================================================================================
PYTHON INSTALL UBUNTU CONFIGURATION
# Step 1: Update your repositories
sudo apt-get update
# Step 2: Install pip for Python 3
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo apt install python3-pip
# Step 3: Use pip to install virtualenv
sudo pip3 install virtualenv
# Step 4: Launch your Python 3 virtual environment, here the name of my virtual environment will be env3
virtualenv -p python3 env3
# Step 5: Activate your new Python 3 environment. There are two ways to do this
. env3/bin/activate # or source env3/bin/activate which does exactly the same thing
# you can make sure you are now working with Python 3
python -- version
# this command will show you what is going on: the python executable you are using is now located inside your virtualenv repository
which python
# Step 6: code your stuff
# Step 7: done? leave the virtual environment

=================================================================
Acessar o Terminal e preparar o ambiente para testar a solucao:

Criar diretorio para simular os testes:

# Criacao do ambiente virtual PYTHON
python -m virtualenv env

ls -la

# Ativar o ambiente virtual
source env/bin/activate
ls -lrt


# Instalacao biblioteca Pub/Sub PYTHON
pip install --upgrade google-cloud-pubsub
google.cloud

# Comandos SHELL para verificar os tópicos
gcloud pubsub topics create my-topic
gcloud pubsub subscriptions create my-sub --topic my-topic

# Comandos pubsub Listar topicos e subscriptions
gcloud pubsub topics list

gcloud pubsub subscriptions list

gcloud info


# Check com os programas Publisher e Subscriber - Python:
python publisher3.py projeto-pubsub my-topic

python subscriber.py projeto-pubsub my-topic


python publisher.py
python subscriber.py


gcloud pubsub subscriptions delete my-sub
gcloud pubsub topics delete my-topic

================================================================================================
Preparando o ambiente para execucao local.
Referência:
https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu

# Add the Cloud SDK distribution URI as a package source
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# Import the Google Cloud Platform public key
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

# Update the package list and install the Cloud SDK
sudo apt-get update && sudo apt-get install google-cloud-sdk


# Inicializar o SDK
# Use o comando gcloud init para executar várias tarefas comuns de configuração do SDK. entre elas:
# autorizar as ferramentas do SDK a acessar o Google Cloud Platform usando as credenciais da sua
# conta de usuário e definir a configuração padrão do SDK.

Para iniciar o SDK:
Execute o seguinte comando em um prompt:

gcloud init

[1] us-east1-b
 [2] us-east1-c
 [3] us-east1-d
 [4] us-east4-c
 [5] us-east4-b
 [6] us-east4-a
 [7] us-central1-c
 [8] us-central1-a
 [9] us-central1-f
 [10] us-central1-b
