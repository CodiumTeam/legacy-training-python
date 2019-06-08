# Gilded Rose characterization testing

## Description:
This kata has a legacy code to practice writing unit tests and characterization tests.

There is an example test to simplify writing the first test.

You can to run the test with coverage in order to know if all the paths have been executed.

You can to run mutation testing in order to know if all the boundaries have been ensured.

# Business requirements
- At the end of each day items lowers quality and sellIn by one
- Once the sell by date has passed, Quality degrades twice as fast
- The Quality of an item is never negative
- "Aged Brie" actually increases in Quality the older it gets instead of decreasing
- The Quality of an item is never more than 50
- "Sulfuras" never has to be sold nor decreases in Quality (quality and sellIn does not change)
- "Backstage passes": We don’t know the requirements :(


## Goals:
- Write unit tests test that validates the business requirements
- Use the characterization test technique and code coverage to identify the Backstage passes requirements.

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