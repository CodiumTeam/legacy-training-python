# Gilded Rose characterization testing

## Description:
This kata has a legacy code to practice the characterization testing.

There is an example test to simplify writing the first test.

You need to run the test with coverage in order to know if all the paths have been executed.

You need to run mutation testing in order to know if all the boundaries have been ensured.
 

## Goals:
- Identify the requirements while writing the tests without understanding the code.

## Run the tests

    python3 -m unittest

or inside docker

    docker run -v "$PWD:/home" -w /home python python3 -m unittest
    
## Inspired by:
https://github.com/emilybache/GildedRose-Refactoring-Kata/

Emily Bache @emilybache