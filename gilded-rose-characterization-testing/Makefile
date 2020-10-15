.PHONY: default tests docker-tests
default:
	@printf "$$HELP"

run-python2:
	pytest

tests:
	python -m unittest
coverage:
	coverage run -m unittest
	coverage html
	@printf "Please open the report at htmlcov/gilded_rose_gilded_rose_py.html\n"

docker-build:
	@docker build . -t python-coverage
docker-tests:
	@docker run -v ${PWD}:/opt/project -w /opt/project python-coverage make tests
docker-coverage:
	@docker run -v ${PWD}:/opt/project -w /opt/project python-coverage make coverage


define HELP
# Local commands
	- make run\tRun locally using Python3 and Unittest
	- make coverage\tRun the code coverage locally using Python3 and Unittest
	- make run-python2\t\tRun locally using Python2 and Pytest
# Docker commands
	- make docker-build\tBuild the image to run the tests
	- make docker-run\tRun the tests inside docker
	- make docker-coverage\tRun inside docker the code coverage
 Please execute "make <command>". Example make help

endef

export HELP