#!/bin/bash

# Do this to login to ECR, you need a Docker Hub account
#docker login -u YOUR_USERNAME

USERNAME=mavx

docker build -t sampledatasource_etl -f ./sampledatasource/etl/Dockerfile ./sampledatasource
docker tag sampledatasource_etl $USERNAME/sampledatasource_etl:latest
docker push $USERNAME/sampledatasource_etl:latest
