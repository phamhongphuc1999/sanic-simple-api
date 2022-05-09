#! /bin/bash

IMAGE_NAME="sanic_simple_app"
CONTAINER_NAME="sanic_simple_app_container"
ENVIRONMENT="production"

echo "Untag old docker image"
if [ "$(docker images -q $IMAGE_NAME:v1)" ]
then
  docker image tag $IMAGE_NAME:v1 $IMAGE_NAME-old:v1
  docker rmi $IMAGE_NAME:v1
fi

echo "Build new image"
docker build . -t $IMAGE_NAME:v1

echo "Stop and remove old container"
if [ "$(docker ps -aq -f status=running -f name=$CONTAINER_NAME)" ]
then
  docker stop $CONTAINER_NAME
fi

if [ "$(docker ps -aq -f status=exited -f name=$CONTAINER_NAME)" ]
then
  docker rm $CONTAINER_NAME
fi

echo "Remove old image"
if [ "$(docker images -q $IMAGE_NAME-old:v1)" ]
then
  docker rmi $IMAGE_NAME-old:v1
fi

echo "Run new container"
while getopts e: flag
do
  case "${flag}" in
      e) environment=${OPTARG};;
  esac
done

if [ "$environment" ]
then
  ENVIRONMENT=$environment
fi

echo "Run with $ENVIRONMENT environment"
docker run -d -p 3000:3000 --name $CONTAINER_NAME $IMAGE_NAME:v1 "$ENVIRONMENT"

echo Finish!!
