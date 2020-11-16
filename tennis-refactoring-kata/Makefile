.PHONY: default tests docker-tests
default:
	@printf "$$HELP"

tests:
	python3 -m unittest tests/tennis_unittest.py

docker-tests:
	docker run --rm -v ${PWD}:/opt/project -w /opt/project python:3.8 make tests

define HELP
# Local commands
	- make tests\tRun locally using Python3 and Unittest
# Docker commands
	- make docker-tests\tRun inside docker with Python3
 Please execute "make <command>". Example make help

endef

export HELP