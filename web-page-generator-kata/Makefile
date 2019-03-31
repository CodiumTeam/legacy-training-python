default:
	@printf "$$HELP"

run:
	@python web_page_generator/main.py
	@echo "Webpage generated at html/users.html"

run-python3:
	@python3 web_page_generator/main.py
	@echo "Webpage generated at html/users.html"

docker-run:
	docker run -v $(shell pwd):/opt/project python sh -c "cd /opt/project &&  make run-python3"


define HELP
# Local commands
	- make run\t\tRun locally using Python2
	- make run-python3\tRun locally using Python3
# Docker commands
	- make docker-run\tRun inside docker with Python3
 Please execute "make <command>". Example make help

endef

export HELP