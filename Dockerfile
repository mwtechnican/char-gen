FROM python:3.11.1
COPY ./app /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python /app/app.py