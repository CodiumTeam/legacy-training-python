# Weather kata
We cannot control the weather but we can predict it.

This kata has a code that request the weather prediction from Metaweather.

## Goal
- Test coupled code.
- Remove the external dependency when testing in order to make the tests repeatable and fast 

## How to run and see the result
## Run the tests

**Locally** with Python3 on Linux and Mac

    make run

or inside **docker** on **Linux and Mac**

    make docker-run

or inside docker on **Windows**

    docker run -v %cd%:/opt/project -w /opt/project python make run
    

## Authors
Luis Rovirosa [@luisrovirosa](https://www.twitter.com/luisrovirosa)

Jordi Anguela [@jordianguela](https://www.twitter.com/jordianguela)