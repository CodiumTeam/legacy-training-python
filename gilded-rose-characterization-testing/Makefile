.PHONY: default tests docker-tests mutation
default:
	@printf "$$HELP"

tests:
	python -m unittest
coverage:
	coverage run --source=gilded_rose -m unittest
	coverage report
	coverage html
	@printf "To visualize the lines open the report at htmlcov/index.html\n"

mutation:
	mutmut run --paths-to-mutate gilded_rose || true
	mutmut results

docker-build:
	@docker build . -t python-coverage
docker-tests:
	@docker run --rm -v "${PWD}:/opt/project" -w /opt/project python-coverage make tests
docker-coverage:
	@docker run --rm -v "${PWD}:/opt/project" -w /opt/project python-coverage make coverage
docker-mutation:
	@docker run -v "${PWD}:/opt/project" -w /opt/project python-coverage make mutation


define HELP
# Local commands
	- make run\tRun locally using Python3 and Unittest
	- make coverage\tRun the code coverage locally using Python3 and Unittest
	- make mutation\tRun the mutations locally using Python3
# Docker commands
	- make docker-build\tBuild the image to run the tests
	- make docker-run\tRun the tests inside docker
	- make docker-coverage\tRun inside docker the code coverage
	- make docker-mutation\tRun the mutations inside docker
 Please execute "make <command>". Example make help

endef

export HELP