FROM python:3.7
COPY ./pdp /pdp
WORKDIR /pdp
RUN pip install -U pip
RUN pip install -r requirements.txt
#CMD python3 wsgi.py