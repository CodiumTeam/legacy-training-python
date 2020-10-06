@echo off

CALL :validateDocker
CALL :validateKata web-page-generator-kata "docker run -v %CD%:/opt/project -w /opt/project python:3.8-alpine make run"
CALL :validateKata tennis-refactoring-kata "docker run -v %CD%:/opt/project -w /opt/project python:3.8-alpine make tests"
REM CALL :validateKata user-registration-refactoring-kata "cd user-registration-refactoring-kata" "make docker-build" "make docker-tests"
REM CALL :validateKata weather-kata "cd weather-kata" "make docker-build" "make docker-tests"
REM CALL :validateKata trip-service-kata "cd trip-service-kata" "make docker-tests"
REM CALL :validateKata gilded-rose-golden-master "cd gilded-rose-golden-master" "make docker-run"
REM CALL :validateKata trivia-golden-master "cd trivia-golden-master" "make docker-run"
REM CALL :validateKata print-date-kata "cd print-date-kata" "make docker-build" "make docker-tests"

goto :eof

:validateKata
    echo Validating %1...
    pushd %1
    CALL %~2
    popd
goto :eof

:validateDocker
    echo Validating docker running...
    docker ps >NUL: 2>NUL:
    IF ERRORLEVEL 1 (
      echo Error
      echo Are you sure that you have docker running?
      goto :eof
    ) else (
      echo "Ok"
    )

    echo Validating docker mount permissions...
    docker run --rm -v "%CD%":/opt -w /opt python:alpine ls >NUL: 2>NUL:
    IF ERRORLEVEL 1 (
      echo Error
      echo Are you sure that you have permissions to mount your volumes?
      goto :eof
    ) else (
      echo Ok
    )
goto :eof

