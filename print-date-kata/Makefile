default:
	@printf "$$HELP"

run-python2:
	pytest

run:
	python -m unittest tests/print_date_test.py
coverage:
	pytest --cov=print_date tests
	coverage html
	@printf "Please open the report at htmlcov/index.html\n"

docker-build:
	@docker build . -t python-coverage
docker-run:
	@docker run -v $(shell pwd):/opt/project -w /opt/project python-coverage make run
docker-coverage:
	@docker run -v $(shell pwd):/opt/project -w /opt/project python-coverage make coverage

docker-win-run:
	docker run -v %cd%:/opt/project -w /opt/project python-coverage make run

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