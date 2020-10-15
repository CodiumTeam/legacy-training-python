.PHONY: default tests docker-tests mutation
default:
	@printf "$$HELP"

run-python2:
	pytest

tests:
	python -m unittest
coverage:
	coverage run --source=gilded_rose -m unittest
	coverage report
	coverage html
	@printf "To visualize the lines open the report at htmlcov/index.html\n"

mutation:
	mutmut run --paths-to-mutate gilded_rose

docker-build:
	@docker build . -t python-coverage
docker-tests:
	@docker run -v ${PWD}:/opt/project -w /opt/project python-coverage make tests
docker-coverage:
	@docker run -v ${PWD}:/opt/project -w /opt/project python-coverage make coverage
docker-mutation:
	@docker run -v ${PWD}:/opt/project -w /opt/project python-coverage make mutation


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