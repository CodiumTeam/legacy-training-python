.PHONY: default
default: docker-tests

.PHONY: docker-tests
docker-tests:
	@docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python make tests

.PHONY: docker-coverage
docker-coverage:
	@docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python make coverage

.PHONY: docker-mutation
docker-mutation:
	@docker run -v "${PWD}:/code" codiumteam/legacy-training-python make mutation

.PHONY: docker-mutate
docker-mutate:
	@docker run -v "${PWD}:/code" codiumteam/legacy-training-python make mutate

.PHONY: tests
tests:
	python -m unittest

.PHONY: coverage
coverage:
	coverage run --source=gilded_rose -m unittest
	coverage report
	coverage html
	@printf "To visualize the lines open the report at htmlcov/index.html\n"

.PHONY: mutation
mutation:
	mutmut run --paths-to-mutate gilded_rose || true
	mutmut results

.PHONY: mutate
mutate:
	mutmut apply <write_the_id>