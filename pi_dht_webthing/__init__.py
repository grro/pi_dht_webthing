from string import Template
from pi_dht_webthing.app import App
from pi_dht_webthing.dht_webthing import run_server


PACKAGENAME = 'pi_dht_webthing'
ENTRY_POINT = "dht"
DESCRIPTION = "A web connected DHT sensor reading temperature and humidity values on Raspberry Pi"


UNIT_TEMPLATE = Template('''
[Unit]
Description=$packagename
After=syslog.target network.target

[Service]
Type=simple
ExecStart=$entrypoint --command listen --hostname $hostname --verbose $verbose --port $port --gpio $gpio
SyslogIdentifier=$packagename
StandardOutput=syslog
StandardError=syslog
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
''')




class DhtApp(App):

    def do_add_argument(self, parser):
        parser.add_argument('--gpio', metavar='gpio', required=False, type=int, help='the gpio number wired to the device')
        parser.add_argument('--name', metavar='name', required=False, default='Motion Sensor', type=str, help='the name of the sensor')


    def do_additional_listen_example_params(self):
        return "--gpio 14"

    def do_process_command(self, command:str, hostname: str, port: int, verbose: bool, args) -> bool:
        if command == 'listen' and (args. gpio is not None):
            print("running " + self.packagename + "/" + args.name + " on " + hostname + "/" + str(port) + "/gpio " + str(args.gpio))
            run_server(hostname, port, int(args.gpio), self.description)
            return True
        elif args.command == 'register' and (args.gpio is not None):
            print("register " + self.packagename + "/" + args.name  + " on " + hostname + "/" + str(port) + "/gpio " + str(args.gpio) + " and starting it")
            unit = UNIT_TEMPLATE.substitute(packagename=self.packagename, entrypoint=self.entrypoint, hostname=hostname, port=port, verbose=verbose, gpio=args.gpio)
            self.unit.register(hostname, port, unit)
            return True
        else:
            return False


def main():
    DhtApp(PACKAGENAME, ENTRY_POINT, DESCRIPTION).handle_command()


if __name__ == '__main__':
    main()
