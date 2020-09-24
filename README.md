# pi_dht_webthing
A web connected humidity and temperature sensor

This project provides a [webthing API](https://iot.mozilla.org/wot/) to a DHT11 or DHT22 humidity and temperature sensor running on a Rasperry Pi. 


By doing this a http endpoint is provided which supports reading the humidity and temperature sensor values via http. E.g. 

```
# webthing has been started on host 192.168.0.23

curl http://192.168.0.23:9050/properties 

{
   "temperature" : 17.3,
   "humidity" : 79.9
}
```

Regarding the hardware setup please tutorials such as [Using the DHT11 temperaturesensor with the raspberry pi](https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/)

To install this software you ma use PIP such as shown below
```
pip install pi_dht_webthing
```

After this installation you may start the webthing via your code or via command line. E.g
```
sudo dht --command listen --port 9050 --gpio 33
```
Here the webthing API will be exposed using the local port 8080 and connecting the DHT signal pin 33

You may also use the register command to register and start the webthing service as systemd unit. By doing this the wething service will be started automatically on boot
```
sudo dht --command register --port 9050 --gpio 33
```  