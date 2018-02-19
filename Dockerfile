FROM python:alpine

RUN apk update && apk upgrade && \

    apk add --no-cache git

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/ann2014/data602-assignment1 /usr/src/app/flask-trader

CMD [ "python", "/usr/src/app/flask-trader/trader.py" ]
