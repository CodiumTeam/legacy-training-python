.PHONY: default
default: docker-tests

.PHONY: docker-tests
docker-tests:
	docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python python manage.py test test