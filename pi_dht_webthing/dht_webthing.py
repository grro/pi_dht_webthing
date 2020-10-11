from webthing import (SingleThing, Property, Thing, Value, WebThingServer)
import logging
import os
import tornado.ioloop
import Adafruit_DHT


class DhtSensor(Thing):

    # regarding capabilities refer https://iot.mozilla.org/schemas
    # there is also another schema registry http://iotschema.org/docs/full.html not used by webthing

    def __init__(self, gpio_number, decription):
        Thing.__init__(
            self,
            'urn:dev:ops:dhtSensor-1',
            'Humidity and Temperature Sensor',
            ['TemperatureSensor', 'HumiditySensor'],
            decription
        )

        self.sensor = Adafruit_DHT.DHT22
        self.gpio_number = gpio_number
        self.humidity = Value(0.0)
        self.add_property(
            Property(self,
                     'humidity',
                     self.humidity,
                     metadata={
                         '@type': 'HumidityProperty',
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
                         '@type': 'TemperatureProperty',
                         'title': 'Temperature',
                         'type': 'number',
                         'description': 'The current temperature',
                         'unit': 'degree celsius',
                         'readOnly': True,
                     }))

        self.timer = tornado.ioloop.PeriodicCallback(self.__measure, (60 * 1000))  # 1 min
        self.timer.start()

    def __measure(self):
        try:
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.gpio_number)
            if humidity is not None:
                self.humidity.notify_of_external_update(round(humidity, 1))
                logging.debug('humidity ' + str(humidity))
            if temperature is not None:
                self.temperature.notify_of_external_update(round(temperature, 1))
                logging.debug('temperature ' + str(temperature))
        except Exception as e:
            logging.error(e)

    def cancel_measure_task(self):
        self.timer.stop()


def run_server(port, gpio_number, description):
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    dht_sensor = DhtSensor(gpio_number, description)
    server = WebThingServer(SingleThing(dht_sensor), port=port)
    try:
        logging.info('starting the server')
        server.start()
    except KeyboardInterrupt:
        logging.info('stopping the server')
        dht_sensor.cancel_measure_task()
        server.stop()
        logging.info('done')



