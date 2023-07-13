.PHONY: default
default: docker-run

.PHONY: run
run:
	@python trivia/main.py

.PHONY: coverage
coverage:
	pytest --cov=trivia tests
	coverage html
	@printf "Please open the report at htmlcov/index.html\n"

.PHONY: golden-master
golden-master:
	@python trivia/main.py

.PHONY: docker-run
docker-run:
	@docker run --rm -v "${PWD}:/code" -w /code python:3.8 make run

.PHONY: docker-golden-master
docker-golden-master:
	@docker run --rm -v "${PWD}:/code" -w /code python:3.8 make golden-master
