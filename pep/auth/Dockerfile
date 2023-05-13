FROM python:3.7
COPY ./auth /auth
WORKDIR /auth
RUN pip install -U pip
RUN pip install -r requirements.txt
#CMD python3 wsgi.py