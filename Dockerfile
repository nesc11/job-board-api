FROM python:3.13-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 80

COPY ./app /code/app

CMD ["fastapi", "dev", "app/main.py", "--port", "80", "--host", "0.0.0.0"]