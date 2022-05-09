#! /bin/bash

CONTAINER_NAME="sanic_simple_app"
SQL_CONTAINER_NAME="dev_sanic_sql_container"
CROSS_CHAIN_NETWORK="sanic_simple_network"

echo "Create cross chain bridge network"
if [ "$(docker network ls -q -f name=$CROSS_CHAIN_NETWORK)" ]
then
  echo "Network is already exist. Skip create!!!"
else
  docker network create $CROSS_CHAIN_NETWORK
fi

echo "Run mongo database container"
if [ "$(docker ps -q -f name=$SQL_CONTAINER_NAME)" ]
then
  echo "Mongo database container is already exist"
  if [ "$(docker ps -aq -f status=exited -f name=$SQL_CONTAINER_NAME)" ]
  then
    docker start $SQL_CONTAINER_NAME
  fi
else
  docker-compose -f docker-compose-mongodb.yaml up -d
fi

echo "Build and run bridge container"
./run.sh -e development

echo "Connect sql container to cross chain bridge network"
if [ "$(docker container inspect "$SQL_CONTAINER_NAME" --format='{{json .NetworkSettings.Networks.'$CROSS_CHAIN_NETWORK'}}')" == "null" ]
then
  docker network connect "$CROSS_CHAIN_NETWORK" "$SQL_CONTAINER_NAME"
fi

echo "Connect bridge container to cross chain bridge network"
if [ "$(docker container inspect "$CONTAINER_NAME" --format='{{json .NetworkSettings.Networks.'$CROSS_CHAIN_NETWORK'}}')" == "null" ]
then
  docker network connect "$CROSS_CHAIN_NETWORK" "$CONTAINER_NAME"
fi
