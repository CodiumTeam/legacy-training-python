FROM python:3.12

RUN pip3 install coverage
RUN pip3 install pytest-cov
RUN pip3 install mutmut
RUN pip3 install django

WORKDIR /code
VOLUME ["/code"]