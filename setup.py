from setuptools import setup

setup(
    name='pi_dht_webthing',
    packages=['pi_dht_webthing'],
    version_config={
        "version_format": "{tag}.dev{sha}",
        "starting_version": "0.0.1"
    },
    setup_requires=['better-setuptools-git-version'],
    description='A web connected DHT sensor reading temperature and humidity values on Raspberry Pi',
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
        'webthings', 'dht', 'dht11', 'dht22', 'home automation', 'humidity sensor', 'temperature sensor', 'raspberry'
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

