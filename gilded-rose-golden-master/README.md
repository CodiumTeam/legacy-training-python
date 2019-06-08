# Gilded Rose characterization testing

## Description:
This kata has a legacy code to practice writing a Golden Master piece.

Write your code inside the gilded_rose/main.py

# Business requirements
You don't need the business requirements.

## Goals:
- Write a code to generate an output that you need to be sure the code behaviour does not change.
- Write an script to automate the test execution.

## Run the tests

**Locally** with Python3 on Linux and Mac

    make run

or inside **docker** on **Linux and Mac**

    make docker-run

or inside docker on **Windows**

    docker run -v %cd%:/opt/project -w /opt/project python make run
    
## Inspired by:
https://github.com/emilybache/GildedRose-Refactoring-Kata/

Emily Bache @emilybache