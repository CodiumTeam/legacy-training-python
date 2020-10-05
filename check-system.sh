#!/bin/bash
FAILED=false
OUTPUT=""
function printStatus() {
  if [ $? -ne 0 ]; then
    echo "Error"
    echo "$OUTPUT"
    FAILED=true
  else
    echo "OK"
  fi
}

echo -n "Validating web-page-generator-kata..............."
OUTPUT=$(cd web-page-generator-kata && make docker-run 2>&1)
printStatus

echo -n "Validating tennis-refactoring-kata..............."
OUTPUT=$(cd tennis-refactoring-kata && make docker-tests 2>&1)
printStatus

echo -n "Validating user-registration-refactoring-kata...."
OUTPUT=$(cd user-registration-refactoring-kata && make docker-build && make docker-tests 2>&1)
printStatus

echo -n "Validating weather-kata.........................."
OUTPUT=$(cd weather-kata && make docker-build && make docker-tests 2>&1)
printStatus

echo -n "Validating trip-service-kata....................."
OUTPUT=$(cd trip-service-kata && make docker-tests 2>&1)
printStatus

echo -n "Validating gilded-rose-golden-master............."
OUTPUT=$(cd gilded-rose-golden-master && make docker-run 2>&1)
printStatus

echo -n "Validating trivia-golden-master.................."
OUTPUT=$(cd trivia-golden-master && make docker-run 2>&1)
printStatus

echo -n "Validating print-date-kata......................."
OUTPUT=$(cd print-date-kata && make docker-build && make docker-tests 2>&1)
printStatus

if $FAILED; then
  echo -e "\n\nPlease send an email with the problem you have to info@codium.team\n"
else
  echo "Congratulations! You are ready for the training!"
fi
