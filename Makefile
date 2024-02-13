.PHONY: docker-build
docker-build:
	docker build -t codiumteam/legacy-training-python .

.PHONY: docker-push
docker-push:
	docker push codiumteam/legacy-training-python