.PHONY: default
default: docker-run

.PHONY: docker-run
docker-run:
	docker run --rm -v "${PWD}:/code" codiumteam/legacy-training-python make run

.PHONY: run
run:
	python3 web_page_generator/main.py
	@echo "Webpage generated at html/users.html"
