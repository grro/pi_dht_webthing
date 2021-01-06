FROM python:3.9.1-alpine

ENV port 8070
ENV name dht
ENV verbose False


ADD . /tmp/
WORKDIR /tmp/
RUN  python /tmp/setup.py install
WORKDIR /
RUN rm -r /tmp/

CMD dht --command listen --port $port --gpio $gpio --name $name --verbose $verbose