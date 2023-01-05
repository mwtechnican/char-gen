FROM python:3.11.1
COPY ./app /app
ADD . /app
WORKDIR /app
RUN pip install -r app/requirements.txt
CMD waitress-serve --host 0.0.0.0 app:app