# Weather kata
We cannot control the weather but we can predict it.

This kata has a code that request the weather prediction from Metaweather.

## Goal
- Test coupled code.
- Remove the external dependency when testing in order to make the tests repeatable and fast 

## How to run and see the result
## Locally

### on Linux and Mac
Run the tests

    make run

Run the code coverage

    make coverage
    
### on Windows
Run the tests
    
    python -m unittest tests/weather_test.py
    
Run the code coverage

    pytest --cov=weather tests
	coverage html
	
## Docker

### on Linux and Mac
Generate the image

    make docker-build

Run the tests
    
    make docker-run

Run the code coverage
    
    make docker-coverage

### on Windows
Generate the image

    docker build . -t python-coverage

Run the tests
    
    docker run -v %cd%:/opt/project -w /opt/project python-coverage make run

Run the code coverage

    docker run -v %cd%:/opt/project -w /opt/project python-coverage make coverage
    

## Authors
Luis Rovirosa [@luisrovirosa](https://www.twitter.com/luisrovirosa)

Jordi Anguela [@jordianguela](https://www.twitter.com/jordianguela)