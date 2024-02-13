.PHONY: default
default: docker-tests

.PHONY: tests
tests:
	python3 -m unittest tests/trip_service_test.py

docker-tests:
	docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python make tests
