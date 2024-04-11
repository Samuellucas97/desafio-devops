# include .env

all: run
.PHONY: all build run clean

build: clean
	@echo
	@echo "******************** BUILDING & TAGGING DOCKER IMAGE **********************************"
	docker compose up -d --build
	@echo
	@echo
	docker ps
	@echo


run:	 
	@echo
	@echo "******************** RUNNING DOCKER INSTANCE **********************************"
	docker compose up -d
	@echo
	@echo
	docker ps
	@echo


clean:
	@echo
	@echo "******************** KILLING CONTAINER **********************************"
	docker compose down --volumes
	@echo
	docker ps
	@echo
