FROM python:alpine

RUN apk update && apk upgrade && \
    apk add --no-cache git

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN git clone https://github.com/ann2014/trader-web /usr/src/app/trader-web
EXPOSE 5000
CMD [ "python", "/usr/src/app/trader-web/app.py" ]
