# pi_dht_webthing
A web connected humidity and temperature sensor

This project provides a [webthing API](https://iot.mozilla.org/wot/) to a [DHT11 or DHT22](https://learn.adafruit.com/dht) humidity and temperature sensor 
running on a Raspberry Pi. As a webthing, the DHT sensor can be discovered and used by 
*home automation systems* or custom solutions supporting the webthing API.  

The pi_dht_webthing exposes an http webthing endpoint which supports reading the humidity and temperature sensor values via http. E.g. 
```
# webthing has been started on host 192.168.0.23

curl http://192.168.0.23:9050/properties 

{
   "temperature" : 17.3,
   "humidity" : 79.9
}
```

A RaspberryPi/DHTxx hardware setup and wiring may look like [DHT22 example](docs/layout.png). 

To install this software you may use [PIP](https://realpython.com/what-is-pip/) package manager such as shown below
```
sudo pip install pi_dht_webthing
```

After this installation you may start the webthing http endpoint inside your python code or via command line using
```
sudo dht --command listen --port 9050 --gpio 2
```
Here, the webthing API will be bind to the local port 9050 and be connected to the DHTxx signal pin using gpio 2

Alternatively to the *listen* command, you can use the *register* command to register and start the webthing service as systemd unit. 
By doing this the webthing service will be started automatically on boot. Starting the server manually using the *listen* command is no longer necessary. 
```
sudo dht --command register --port 9050 --gpio 2
```  
