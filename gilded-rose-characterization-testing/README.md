# Gilded Rose characterization testing

## Description:
This kata has a legacy code to practice writing unit tests and characterization tests.

There is an example test to simplify writing the first test.

You can to run the test with coverage in order to know if all the paths have been executed.

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


## How to run and see the result
## Locally
### on Linux and Mac
Run the tests

    make tests

Run the code coverage

    make coverage
    
### on Windows
Open the Makefile and copy and paste the lines below each command.
	
## Docker

### on Linux and Mac
Generate the image

    make docker-build

Run the tests
    
    make docker-tests

Run the code coverage
    
    make docker-coverage

### on Windows
Open the Makefile and copy and paste the lines below each command.
    
## Inspired by:
https://github.com/emilybache/GildedRose-Refactoring-Kata/

Emily Bache @emilybache