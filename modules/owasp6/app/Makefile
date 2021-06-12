PROJECT_NAME ?= OWASP6
VERSION = $(shell python3.9 setup.py --version | tr '+' '-')
PROJECT_NAMESPACE ?= owasp6
REGISTRY_IMAGE ?= $(PROJECT_NAMESPACE)/$(PROJECT_NAME)

all:
	@echo "make dev         	- Create & run development environment"
	@echo "make run         	- Create & run development environment in terminal (realtime)"
	@echo "make migrate     	- Apply all migrations"
	@echo "make makemigrations	- Create all migrations"
	@exit 0

_clean_makefile:
	rm -fr *.egg-info dist

dev:
	uvicorn main:app --reload

run:
	uvicorn main:app --reload

makemigrations:
	alembic  revision --autogenerate

migrate:
	alembic upgrade head
