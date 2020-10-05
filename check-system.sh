#!/bin/bash
ERROR=""
OUTPUT=""
function printStatus() {
  if [ $? -ne 0 ]; then
    echo "Error"
    ERROR="${ERROR} \n\n${OUTPUT}"
  else
    echo "Ok"
  fi
}

function validateKata() {
    echo -n "Validating $1..."
    OUTPUT=$($2 2>&1 && $3 2>&1 && $4 2>&1)
    printStatus
}

validateKata web-page-generator-kata "cd web-page-generator-kata" "make docker-run"
validateKata tennis-refactoring-kata "cd tennis-refactoring-kata" "make docker-tests"
validateKata user-registration-refactoring-kata "cd user-registration-refactoring-kata" "make docker-build" "make docker-tests"
validateKata weather-kata "cd weather-kata" "make docker-build" "make docker-tests"
validateKata trip-service-kata "cd trip-service-kata" "make docker-tests"
validateKata gilded-rose-golden-master "cd gilded-rose-golden-master" "make docker-run"
validateKata trivia-golden-master "cd trivia-golden-master" "make docker-run"
validateKata print-date-kata "cd print-date-kata" "make docker-build" "make docker-tests"

if [ -z "$ERROR" ]; then
  echo "Congratulations! You are ready for the training!"
else
  echo -e "----------------------------------------------------------\n\n$ERROR"
  echo -e "\n\nPlease send an email with the problem you have to info@codium.team\n"
fi
