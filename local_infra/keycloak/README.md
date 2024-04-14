docker run -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:24.0.2 start-dev

docker run --detach --rm -p ${DOCKER_HOST_PORT}:${DOCKER_INTERNAL_PORT} -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin --name ${CONTAINER_NAME} ${APP_DOCKER}:${DOCKER_IMAGE_VERSION}
	