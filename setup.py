from setuptools import setup
from os import path



PACKAGENAME = 'pi_dht_webthing'
ENTRY_POINT = "dht"
DESCRIPTION = "A web connected DHT sensor reading temperature and humidity values on Raspberry Pi"



this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pi_dht_webthing',
    packages=['pi_dht_webthing'],
    version_config={
        "version_format": "{tag}.dev{sha}",
        "starting_version": "0.0.1"
    },
    setup_requires=['better-setuptools-git-version'],
    description='A web connected DHT sensor reading temperature and humidity values on Raspberry Pi',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Gregor Roth',
    author_email='gregor.roth@web.de',
    url='https://github.com/grro/pi_dht_webthing',
    entry_points={
        'console_scripts': [
            'dht=pi_dht_webthing:main'
        ]
    },
    keywords=[
        'webthings', 'dht', 'dht11', 'dht22', 'home automation', 'humidity sensor', 'temperature sensor', 'raspberry', 'pi'
    ],
    install_requires=[
        'webthing',
        'Adafruit-DHT'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
)

