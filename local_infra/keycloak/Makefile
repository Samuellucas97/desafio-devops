CONTAINER_NAME=keycloak_server
APP_DOCKER=quay.io/keycloak/keycloak
DOCKER_IMAGE_VERSION=24.0.2
DOCKER_HOST_PORT=8080
DOCKER_INTERNAL_PORT=8080

all: run
.PHONY: all run clean

run: clean	 
	@echo
	@echo "******************** RUNNING DOCKER INSTANCE **********************************"
	docker run --net=host --detach --rm  --name ${CONTAINER_NAME} -p ${DOCKER_HOST_PORT}:${DOCKER_INTERNAL_PORT} -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:24.0.2 start-dev 
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