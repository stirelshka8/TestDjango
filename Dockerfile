FROM python:3.10

ENV PYTHONUNBUFFERED 1

COPY ./req.txt /app/req.txt
RUN pip install -r /app/req.txt

COPY . /app
WORKDIR /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
