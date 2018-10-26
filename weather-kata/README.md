# Run with docker

## Build the image once
docker build -t pytest .

## Run the tests
docker run -v "$PWD":/home/pytest pytest pytest -s