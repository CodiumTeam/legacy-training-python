default:
	@printf "$$HELP"

run:
	pytest

run-python3:
	python3 -m unittest tests/tennis_unittest.py

docker-run:
	docker run -v $(shell pwd):/opt/project python sh -c "cd /opt/project &&  make run-python3"

define HELP
# Local commands
	- make run\t\tRun locally using Python2 and Pytest
	- make run-python3\tRun locally using Python3 and Unittest
# Docker commands
	- make docker-run\tRun inside docker with Python3
 Please execute "make <command>". Example make help

endef

export HELP