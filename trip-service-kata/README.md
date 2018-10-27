# Trip Service Kata

## Description:
This kata simulates a social network of trips.

There are some couplings inside the [TripService](./tripservice/trip_service.py) that we need to use the dependency-breaking techniques that we have learned.

We want to be able to test TripService and when we have good test coverage we will refactor to improve the code design.

We only can change TripService class.

## Goals:
- How to break pain code in order to test it.
- Practice: 
  - Extract and override
  - Extract interface
  - Parametrize constructor
  - Introduce static setter 

## Install the dependencies

    pip install virtualenv
    virtualenv virtualenv
    source virtualenv/bin/activate
    pip install pytest

## Run the tests with

    make test

## Original source code from:
https://github.com/sandromancuso/trip-service-kata
Sandro Mancuso @sandromancuso


