# pi_dht_webthing
A web connected humidity and temperature sensor

This project provides a [webthing API](https://iot.mozilla.org/wot/) to a DHT11 or DHT22 humidity and temperature sensor running on a Rasperry Pi. 


By doing this a http endpoint is provided which supports reading the humidity and temperature sensor vi http. E.g. 

```
curl http://192.168.1.48:9050/ 

{
   "title" : "Humidity and Temperature Sensor",
   "base" : "http://192.168.1.48:9050/",
   "events" : {},
   "security" : "nosec_sc",
   "@type" : [
      "TemperatureSensor",
      "HumiditySensor"
   ],
   "properties" : {
      "temperature" : {
         "description" : "The current temperature in %",
         "links" : [
            {
               "href" : "/properties/temperature",
               "rel" : "property"
            }
         ],
         "readOnly" : true,
         "unit" : "degree celsius",
         "type" : "number",
         "title" : "Temperature",
         "@type" : "LevelProperty"
      },
      "humidity" : {
         "title" : "Humidity",
         "readOnly" : true,
         "maximum" : 100,
         "description" : "The current humidity in %",
         "@type" : "LevelProperty",
         "minimum" : 0,
         "type" : "number",
         "unit" : "percent",
         "links" : [
            {
               "rel" : "property",
               "href" : "/properties/humidity"
            }
         ]
      }
   },
   "links" : [
      {
         "href" : "/properties",
         "rel" : "properties"
      },
      {
         "rel" : "actions",
         "href" : "/actions"
      },
      {
         "rel" : "events",
         "href" : "/events"
      },
      {
         "rel" : "alternate",
         "href" : "ws://192.168.1.48:9050/"
      }
   ],
   "@context" : "https://iot.mozilla.org/schemas",
   "actions" : {},
   "securityDefinitions" : {
      "nosec_sc" : {
         "scheme" : "nosec"
      }
   },
   "id" : "urn:dev:ops:dht22Sensor-1234",
   "description" : "A web connected humidity and temperature sensor"
}
```

Regarding the hardware setup please tutorials such as [Using the DHT11 temperaturesensor with the raspberry pi](https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/)

To install this software you ma use PIP such as shown below
```
pip install pi_dht_webthing
```

After this installation you may start the webthing via your code or via command line. E.g
```
sudo dht --command listen --port 8080 --gpio 33
```
Here the webthing API will be exposed using the local port 8080 and connecting the DHT signal pin 33

You may also use the register command to register and start the webthing service as systemd unit
```
sudo dht --command register --port 8080 --gpio 33
```  