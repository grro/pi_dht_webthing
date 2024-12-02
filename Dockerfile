FROM python:3-alpine

ENV port 8070
ENV name dht


RUN cd /etc
RUN mkdir app
WORKDIR /etc/app
ADD *.py /etc/app/
ADD requirements.txt /etc/app/.
RUN pip install -r requirements.txt

CMD python /etc/app/dht_webthing.py $port $name

