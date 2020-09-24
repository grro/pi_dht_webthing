from setuptools import setup

setup(
    name='pi_dht_webthing',
    packages=['pi_dht_webthing'],
    version="0.0.1",
    description='A web connected humidity and temperature sensor',
    long_description='',
    license='MIT',
    author='Gregor Roth',
    author_email='gregor.roth@web.de',
    url='https://tobeset',
    download_url="https://tobeset",
    entry_points={
        'console_scripts': [
            'dht=pi_dht_webthing:main'
        ]
    },
    keywords=[
        'webthings', 'dht', 'dht11', 'dht22', 'home automation', 'raspberry'
    ],
    install_requires=[
        'webthing',
        'Adafruit-DHT'
    ]
)

