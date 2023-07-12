.PHONY: default
default: docker-tests
	@printf "$$HELP"

.PHONY: tests
tests:
	python -m unittest tests/print_date_test.py

.PHONY: coverage
coverage:
	pytest --cov=print_date tests
	coverage html
	@printf "Please open the report at htmlcov/index.html\n"

.PHONY: docker-build
docker-build:
	@docker build . -t codiumteam/legacy-training-python:print-date

.PHONY: docker-tests
docker-tests:
	@docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python:print-date make tests

.PHONY: docker-coverage
docker-coverage:
	@docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python:print-date make coverage