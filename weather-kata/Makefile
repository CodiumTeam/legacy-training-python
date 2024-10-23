.PHONY: default
default: docker-tests

.PHONY: docker-tests
docker-tests:
	@docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python make tests

.PHONY: docker-coverage
docker-coverage:
	@docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python make coverage

.PHONY: tests
tests:
	python -m unittest tests/test_weather.py

.PHONY: coverage
coverage:
	coverage run --source=weather -m unittest
	coverage report
	coverage html
	@printf "To visualize the lines open the report at htmlcov/index.html\n"
