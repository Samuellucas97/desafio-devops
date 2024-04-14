include .env

CONTAINER_NAME=flask_app
FLASK_APP_DOCKER=app
DOCKER_IMAGE_VERSION=1.0
DOCKER_HOST_PORT=8000
DOCKER_INTERNAL_PORT=8000
DOCKER_REGISTRY=docker.io
DOCKER_REGISTRY_REPOSITORY=samuel1797/desafio-devops
DOCKER_REGISTRY_REPOSITORY_TAG=1.0
all: run
.PHONY: all build run clean

build: clean
	@echo
	@echo "******************** BUILDING & TAGGING DOCKER IMAGE **********************************"
	docker build -t ${FLASK_APP_DOCKER}:${DOCKER_IMAGE_VERSION} .
	@echo
	@echo
	docker image ls
	@echo


run: build	 
	@echo
	@echo "******************** RUNNING DOCKER INSTANCE **********************************"
	docker build -t ${FLASK_APP_DOCKER}:${DOCKER_IMAGE_VERSION} .
	docker run --net=host --detach --rm -p ${DOCKER_HOST_PORT}:${DOCKER_INTERNAL_PORT} --name ${CONTAINER_NAME} ${FLASK_APP_DOCKER}:${DOCKER_IMAGE_VERSION}
	@echo
	@echo
	docker ps
	@echo


clean:
	@echo
	@echo "******************** KILLING CONTAINER **********************************"
	docker rm -f ${CONTAINER_NAME}
	@echo
	docker ps
	@echo
	@echo
	@echo "******************** REMOVING DOCKER IMAGE **********************************"
	docker image rm -f ${FLASK_APP_DOCKER}:${DOCKER_IMAGE_VERSION}
	@echo
	docker image ls
	@echo


publish:
	@echo
	@echo "******************** BUILDING & TAGGING DOCKER IMAGE **********************************"
	docker build -t ${DOCKER_REGISTRY_REPOSITORY}:${DOCKER_REGISTRY_REPOSITORY_TAG} .
	@echo
	docker image ls
	@echo
	docker login -u ${DOCKER_REGISTRY_LOGIN} -p ${DOCKER_REGISTRY_TOKEN} ${DOCKER_REGISTRY}
	@echo
	@echo "******************** PUSHING IMAGE TO THE DOCKERHUB **********************************"
	docker push ${DOCKER_REGISTRY_REPOSITORY}:${DOCKER_REGISTRY_REPOSITORY_TAG}
	@echo
	@echo "******************** BUILDING & TAGGING DOCKER IMAGE AS LATEST **********************************"
	docker build -t ${DOCKER_REGISTRY_REPOSITORY}:latest .
	@echo
	docker image ls
	@echo
	docker login -u ${DOCKER_REGISTRY_LOGIN} -p ${DOCKER_REGISTRY_TOKEN} ${DOCKER_REGISTRY}
	@echo
	@echo "******************** PUSHING LATEST IMAGE TO THE DOCKERHUB **********************************"
	docker push ${DOCKER_REGISTRY_REPOSITORY}:latest
