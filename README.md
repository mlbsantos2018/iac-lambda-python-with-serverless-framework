# CRUD API com AWS Lambda, Python e DynamoDB

Este projeto é uma API CRUD simples usando AWS Lambda, Python, DynamoDB e o Serverless Framework. A API permite criar, ler, atualizar e deletar itens em uma tabela DynamoDB.

## Pré-requisitos

- Node.js e npm
- Python 3.8
- AWS CLI configurado com suas credenciais
- Serverless Framework instalado globalmente

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/mlbsantos2018/iac-lambda-python-with-serverless-framework.git
    cd iac-lambda-python-with-serverless-framework
    ```

2. Instale as dependências do projeto:

    ```bash
    npm install
    ```

3. Instale as dependências Python:

    ```bash
    pip install -r requirements.txt
    ```

## Configuração

Configure o Serverless Framework com suas credenciais AWS se ainda não fez isso:

```bash
serverless config credentials --provider aws --key SEU_ACCESS_KEY --secret SEU_SECRET_KEY
