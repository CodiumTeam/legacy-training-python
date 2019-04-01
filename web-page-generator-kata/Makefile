default:
	@printf "$$HELP"

run-python2:
	@python web_page_generator/main.py
	@echo "Webpage generated at html/users.html"

run:
	python3 web_page_generator/main.py
	@echo "Webpage generated at html/users.html"

docker-run:
	docker run -v $(shell pwd):/opt/project -w /opt/project python make run


define HELP
# Local commands
	- make run\tRun locally using Python3
	- make run-python2\t\tRun locally using Python2
# Docker commands
	- make docker-run\tRun inside docker with Python3
 Please execute "make <command>". Example make help

endef

export HELP