FLASK_APP_DOCKER=app
DOCKER_IMAGE_VERSION=1.0

all: build
.PHONY: all 

build: 
	@echo
	@echo "******************** BUILDING & TAGGING DOCKER IMAGE **********************************"
	docker build -t ${FLASK_APP_DOCKER}:${DOCKER_IMAGE_VERSION} .
	@echo
	@echo
	docker image ls
	@echo


	

	