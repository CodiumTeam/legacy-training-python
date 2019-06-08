default:
	@printf "$$HELP"

run:
	python3 gilded_rose/main.py

golden-master:
	python3 gilded_rose/main.py

docker-run:
	docker run -v $(shell pwd):/opt/project -w /opt/project python make run

docker-golden-master:
	docker run -v $(shell pwd):/opt/project -w /opt/project python make golden-master

docker-win-run:
	docker run -v %cd%:/opt/project -w /opt/project python make run

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