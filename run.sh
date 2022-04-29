#!/bin/bash
VOLUMES="${docker volume ls | postgres-flask | awk '{print $2}'}"

if [ -n "$VOLUMES"]; then
    docker volume create postgres-flask
fi

docker-compose build

docker-compose down

docker-compose up