.PHONY: default
default: docker-run

.PHONY: docker-run
docker-run:
	docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python make run

.PHONY: docker-golden-master
docker-golden-master:
	docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python make golden-master

.PHONY: run
run:
	python3 gilded_rose/main.py

.PHONY: golden-master
golden-master:
	python3 gilded_rose/main.py
