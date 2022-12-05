FROM python:3.9.10-alpine
RUN apk update

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

# run crond as main process of container
CMD ["python3", "send-email.py"]