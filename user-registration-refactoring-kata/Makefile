docker-build:
	docker build -t django-docker-bootstrap .

docker-start:
	@echo "Please open http://localhost:8000"
	docker run -v $(shell pwd):/opt/project -p 8000:8000 django-docker-bootstrap

docker-tests:
	docker run -v $(shell pwd):/opt/project django-docker-bootstrap ./manage.py test test