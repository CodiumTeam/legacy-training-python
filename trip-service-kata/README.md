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

## How to run and see the result
## Run the tests

**Locally** with Python3 on Linux and Mac

    make tests

or inside **docker** on **Linux and Mac**

    make docker-tests

or on **Windows**

Open the Makefile and copy and paste the lines below each command.

## Original source code from:
https://github.com/sandromancuso/trip-service-kata

Sandro Mancuso @sandromancuso


