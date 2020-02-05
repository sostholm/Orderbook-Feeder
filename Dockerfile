FROM python:alpine

COPY download_orderbook.py /app/
COPY requirements.txt /app/

WORKDIR app

RUN pip install -r requirements.txt

CMD ["python3", "-u", "./download_orderbook.py"]

