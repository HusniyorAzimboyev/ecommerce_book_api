FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app/

CMD ["python","manage.py","runserver","0.0.0.0:8000"]

