#!/bin/bash

source todo-list-aws/bin/activate
set -x

## Creamos red de docker, puede estar creada
docker network create sam

## Borramos el volumen anterior por nombre "dynamodb"
docker rm -v dynamodb --force

## Levantar el contenedor de dynamodb en la red de sam con el nombre de dynamodb
docker run -p 8000:8000 --network sam --name dynamodb -d amazon/dynamodb-local

## Crear la tabla en local, para poder trabajar localmemte
aws dynamodb create-table --table-name local-TodosDynamoDbTable --attribute-definitions AttributeName=id,AttributeType=S --key-schema AttributeName=id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 --endpoint-url http://localhost:8000

## Empaquetar sam
sam build --template ~/environment/todo-list-aws/template.yaml

## Levantar la api en local, en el puerto 8080, dentro de la red de docker sam
sam local start-api --port 8081 --env-vars ~/environment/todo-list-aws/localEnvironment.json --docker-network sam --template ~/environment/todo-list-aws/template.yaml