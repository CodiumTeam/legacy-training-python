.PHONY: default
default: docker-run

.PHONY: docker-run
docker-run:
	@docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python make run

.PHONY: docker-tests
docker-tests:
	@docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python make tests

.PHONY: docker-coverage
docker-coverage:
	@docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python make coverage

.PHONY: docker-golden-master
docker-golden-master:
	@docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python make golden-master

.PHONY: run
run:
	@python -m trivia

.PHONY: tests
tests:
	pytest

.PHONY: coverage
coverage:
	pytest --cov=trivia tests
	coverage html
	@printf "Please open the report at htmlcov/index.html\n"

.PHONY: golden-master
golden-master:
	@python -m trivia
