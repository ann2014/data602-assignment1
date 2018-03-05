FROM python:3.6
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN git clone https://github.com/ann2014/data602-assignment1 /usr/src/app/trader-app
EXPOSE 5000
CMD [ "python", "/usr/src/app/trader-app/console_app.py" ]
