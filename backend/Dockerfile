FROM python:3.8.3-alpine
COPY . .

RUN pip install --upgrade pip
RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install -r ./requirements.txt

WORKDIR src

EXPOSE 8000

CMD python3 -m alembic upgrade head && python3 -m flask --app ./chatapp/server run --port=8000 --host='0.0.0.0'
