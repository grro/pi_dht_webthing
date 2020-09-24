from webthing import (SingleThing, Property, Thing, Value, WebThingServer)
import logging
import tornado.ioloop
import Adafruit_DHT



class Dht22Sensor(Thing):

    def __init__(self, gpio_number):
        Thing.__init__(
            self,
            'urn:dev:ops:dhtSensor-1',
            'Humidity and Temperature Sensor',
            ['TemperatureSensor', 'HumiditySensor'],
            'A web connected humidity and temperature sensor'
        )

        self.sensor = Adafruit_DHT.DHT22
        self.gpio_number = gpio_number
        self.humidity = Value(0.0)
        self.add_property(
            Property(self,
                     'humidity',
                     self.humidity,
                     metadata={
                         '@type': 'LevelProperty',
                         'title': 'Humidity',
                         'type': 'number',
                         'description': 'The current humidity in %',
                         'minimum': 0,
                         'maximum': 100,
                         'unit': 'percent',
                         'readOnly': True,
                     }))

        self.temperature = Value(0)
        self.add_property(
            Property(self,
                     'temperature',
                     self.temperature,
                     metadata={
                         '@type': 'LevelProperty',
                         'title': 'Temperature',
                         'type': 'number',
                         'description': 'The current temperature in %',
                         'unit': 'degree celsius',
                         'readOnly': True,
                     }))

        logging.debug('starting the sensor update looping task')
        self.timer = tornado.ioloop.PeriodicCallback(
            self.measure,
            3000
        )
        self.timer.start()

    def measure(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.gpio_number)
        if humidity is not None:
            self.humidity.notify_of_external_update(round(humidity, 1))
        if temperature is not None:
            self.temperature.notify_of_external_update(round(temperature,1 ))

    def cancel_update_level_task(self):
        self.timer.stop()



def run_server(port, gpio_number):
    dht22Sensor = Dht22Sensor(gpio_number)
    server = WebThingServer(SingleThing(dht22Sensor), port=port)
    try:
        logging.info('starting the server')
        server.start()
    except KeyboardInterrupt:
        logging.debug('canceling the sensor update looping task')
        dht22Sensor.cancel_update_level_task()
        logging.info('stopping the server')
        server.stop()
        logging.info('done')

