FROM python:alpine

RUN pip install telebot

WORKDIR /app

COPY . .

CMD [ "python3", "main.py" ]