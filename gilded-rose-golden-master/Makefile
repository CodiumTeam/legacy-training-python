.PHONY: default run docker-tests
default:
	@printf "$$HELP"

run:
	python3 gilded_rose/main.py

golden-master:
	python3 gilded_rose/main.py

docker-run:
	docker run --rm -v ${PWD}:/opt/project -w /opt/project python:3.8 make run

docker-golden-master:
	docker run --rm -v ${PWD}:/opt/project -w /opt/project python:3.8 make golden-master

define HELP
# Local commands
	- make run\tRun locally using Python3 and Unittest
	- make golden-master\tRun locally using Python3 the golden master generation and validation
# Docker commands
	- make docker-run\tRun inside docker with Python3
	- make docker-golden-master\tRun inside docker using Python3 the golden master generation and validation
 Please execute "make <command>". Example make help

endef

export HELP