# pi_dht_webthing
A web connected humidity and temperature sensor

This project provides a [webthing API](https://iot.mozilla.org/wot/) to a [DHT11 or DHT22](https://learn.adafruit.com/dht) humidity and temperature sensor 
running on a Raspberry Pi. As a webthing, the DHT sensor can be discovered and used by 
*home automation systems* or custom solutions supporting the webthing API.  

The pi_dht_webthing package exposes an http webthing endpoint which supports reading the humidity and temperature sensor values via http. E.g. 
```
# webthing has been started on host 192.168.0.23

curl http://192.168.0.23:9050/properties 

{
   "temperature" : 17.3,
   "humidity" : 79.9
}
```

Regarding the RaspberryPi/DHTxx hardware setup and wiring please refer tutorials such as [Using the DHT11 temperaturesensor with the raspberry pi](https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/)

To install this software you may use PIP such as shown below
```
sudo pip install pi_dht_webthing
```

After this installation you may start the webthing http endpoint inside your python code or via command line using
```
sudo dht --command listen --port 9050 --gpio 33
```
Here, the webthing API will be bind to the local port 8080 and be connected to  the DHTxx signal pin 33

Alternatively to the *listen* command, you can use the *register* command to register and start the webthing service as systemd unit. By doing this the webthing service will be started automatically on boot. 
```
sudo dht --command register --port 9050 --gpio 33
```  
