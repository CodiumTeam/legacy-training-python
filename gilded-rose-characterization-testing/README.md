# Gilded Rose characterization testing

## Description:
This kata has a legacy code to practice writing unit tests and characterization tests.

There is an example test to simplify writing the first test.

You can to run the test with coverage in order to know if all the paths have been executed.

You can to run mutation testing in order to know if all the boundaries have been ensured.

## Goal
- Test business logic using the requirements.
- Use the characterization testing technique to discover the Backstage requirements. 


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

    coverage run weather/weather.py
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
    
## Inspired by:
https://github.com/emilybache/GildedRose-Refactoring-Kata/

Emily Bache @emilybache