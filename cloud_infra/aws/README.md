# AWS - Public Cloud

Este diretório contém os scripts e códigos usados para criação da infraestrutura na nuvem.

## Requisitos

- AWS CLI

## S3 - Terraform state

Estarei utilizando o S3 para armazenar o arquivo de estado do Terraform (i.e., backend state). Esse estado contém todos os recursos (e.g., ec2) gerenciados pelo terraform. Para isso, execute os comandos abaixo visando a criação do recurso:

```bash
$ aws s3api create-bucket --bucket desafiodevopsterraforms3backendbucket --create-bucket-configuration LocationConstraint=us-east-2
{
    "Location": "http://desafiodevopsterraforms3backendbucket.s3.amazonaws.com/"
}
```

## DynamoDB - Terraform

Estarei utilizando o DynamoDB para armazenar o dependency lock. Esse arquivo contém todas as modificações nas configurações.

```bash
$ aws dynamodb create-table --table-name desafio-devops-terraform-lock \
    --attribute-definitions AttributeName=LockID,AttributeType=S \
    --key-schema AttributeName=LockID,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST

{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "LockID",
                "AttributeType": "S"
            }
        ],
        "TableName": "desafio-devops-terraform-lock",
        "KeySchema": [
            {
                "AttributeName": "LockID",
                "KeyType": "HASH"
            }
        ],
        "TableStatus": "CREATING",
        "CreationDateTime": "2024-03-31T18:02:14.597000-03:00",
        "ProvisionedThroughput": {
            "NumberOfDecreasesToday": 0,
            "ReadCapacityUnits": 0,
            "WriteCapacityUnits": 0
        },
        "TableSizeBytes": 0,
        "ItemCount": 0,
        "TableArn": "arn:aws:dynamodb:us-east-2:851725465376:table/desafio-devops-terraform-lock",
        "TableId": "f9a9bccf-b069-44a1-8cc2-fc3554f218ff",
        "BillingModeSummary": {
            "BillingMode": "PAY_PER_REQUEST"
        },
        "DeletionProtectionEnabled": false
    }
}
```

