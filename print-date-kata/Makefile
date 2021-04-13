.PHONY: tests

default:
	@printf "$$HELP"

tests:
	python -m unittest tests/print_date_test.py

tests-python2:
	pytest

coverage:
	pytest --cov=print_date tests
	coverage html
	@printf "Please open the report at htmlcov/index.html\n"

docker-build:
	@docker build . -t python-coverage
docker-tests:
	@docker run --rm -v "${PWD}:/opt/project" -w /opt/project python-coverage make tests
docker-coverage:
	@docker run --rm -v "${PWD}:/opt/project" -w /opt/project python-coverage make coverage

define HELP
# Local commands
	- make tests\tRun locally using Python3 and Unittest
	- make coverage\tRun the code coverage locally using Python3 and Unittest
	- make tests-python2\t\tRun locally using Python2 and Pytest
# Docker commands
	- make docker-build\tBuild the image to run the tests
	- make docker-tests\tRun the tests inside docker
	- make docker-coverage\tRun inside docker the code coverage
 Please execute "make <command>". Example make help

endef

export HELP