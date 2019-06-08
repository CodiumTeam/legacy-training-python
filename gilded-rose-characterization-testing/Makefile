default:
	@printf "$$HELP"

run-python2:
	pytest

run:
	python3 -m unittest tests/gilded_rose_test.py

docker-run:
	docker run -v $(shell pwd):/opt/project -w /opt/project python make run

docker-win-run:
	docker run -v %cd%:/opt/project -w /opt/project python make run

define HELP
# Local commands
	- make run\tRun locally using Python3 and Unittest
	- make run-python2\t\tRun locally using Python2 and Pytest
# Docker commands
	- make docker-run\tRun inside docker with Python3
 Please execute "make <command>". Example make help

endef

export HELP