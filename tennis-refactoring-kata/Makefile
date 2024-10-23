.PHONY: default
default: docker-tests

.PHONY: docker-tests
docker-tests:
	docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python make tests

.PHONY: tests
tests:
	python3 -m unittest tests/tennis_unittest.py
