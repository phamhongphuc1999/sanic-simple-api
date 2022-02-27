PROJECT_NAME=trava_api_v1

# colors
GREEN = $(shell tput -Txterm setaf 2)
YELLOW = $(shell tput -Txterm setaf 3)
WHITE = $(shell tput -Txterm setaf 7)
RESET = $(shell tput -Txterm sgr0)
GRAY = $(shell tput -Txterm setaf 6)
TARGET_MAX_CHAR_NUM = 20

## Create virtual environment. | Config
virtual:
	python3 -m venv /venv

## Install packages with production environment.
installpro:
	pip3 install -r requirements/production.txt

## Install packages with development environment.
installdev:
	pip3 install -r requirements/development.txt

## Run sanic api with production environment. | Run project
runpro:
	python3 main.py production

## Run sanic api with development environment.
rundev:
	python3 main.py development

## Build and run mysql container. | Build and deploy
builddata:
	docker-compose -f docker-compose-mysql.yaml up --buid

## Build sanic image
buildimage:
	docker build . -t sanic_app:v1

## Run docker container.
rundocker:
	docker run -d -p 8000:8000 trava_api:v1

## Shows help. | Help
help:
	@echo ''
	@echo 'Usage:'
	@echo ''
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
		    if (index(lastLine, "|") != 0) { \
				stage = substr(lastLine, index(lastLine, "|") + 1); \
				printf "\n ${GRAY}%s: \n\n", stage;  \
			} \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			if (index(lastLine, "|") != 0) { \
				helpMessage = substr(helpMessage, 0, index(helpMessage, "|")-1); \
			} \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)
	@echo ''
