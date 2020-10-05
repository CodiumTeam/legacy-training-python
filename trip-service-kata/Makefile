default:
	@printf "$$HELP"

tests:
	python3 -m unittest tests/trip_service_test.py

tests-python2:
	pytest

docker-tests:
	docker run -v ${PWD}:/opt/project -w /opt/project python:3.8 make tests

define HELP
# Local commands
	- make tests\tRun locally using Python3 and Unittest
	- make tests-python2\t\tRun locally using Python2 and Pytest
# Docker commands
	- make docker-tests\tRun inside docker with Python3
 Please execute "make <command>". Example make help

endef

export HELP