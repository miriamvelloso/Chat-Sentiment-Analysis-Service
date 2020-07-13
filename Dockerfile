FROM python:3.8.1

ADD ./ ./

RUN pip3 install -r requirements.txt

CMD ["python3","-u","api.py"]