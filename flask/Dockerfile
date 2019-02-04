FROM python:3.6.2

RUN mkdir /log
RUN mkdir /app
WORKDIR /app
COPY apis/. .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt