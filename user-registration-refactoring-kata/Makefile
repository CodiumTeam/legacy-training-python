.PHONY: default
default: docker-tests

.PHONY: docker-build
docker-build:
	docker build -t codiumteam/legacy-training-python:user-registration .

.PHONY: docker-tests
docker-tests:
	docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python:user-registration python manage.py test test