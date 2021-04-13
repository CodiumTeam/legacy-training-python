.PHONY: default run docker-tests
default:
	@printf "$$HELP"

run:
	python trivia/main.py
coverage:
	pytest --cov=trivia tests
	coverage html
	@printf "Please open the report at htmlcov/index.html\n"

golden-master:
	python trivia/main.py

docker-run:
	docker run --rm -v "${PWD}:/opt/project" -w /opt/project python:3.8 make run

docker-golden-master:
	docker run --rm -v "${PWD}:/opt/project" -w /opt/project python:3.8 make golden-master

define HELP
# Local commands
	- make run\tRun locally using Python3
	- make coverage\tRun the test coverage using Python3
	- make golden-master\tRun locally using Python3 the golden master generation and validation
# Docker commands
	- make docker-run\tRun inside docker with Python3
	- make docker-golden-master\tRun inside docker using Python3 the golden master generation and validation
 Please execute "make <command>". Example make help

endef

export HELP