import os
import logging
import argparse
from pi_dht_webthing.dht_webthing import run_server
from pi_dht_webthing.unit import register, deregister, printlog, list_installed


PACKAGENAME = 'pi_dht_webthing'
ENTRY_POINT = "dht"
DESCRIPTION = "A web connected DHT sensor reading temperature and humidity values on Raspberry Pi"


def print_info():
    print("usage " + ENTRY_POINT + " --help for command options")
    print("example commands")
    print(" sudo " + ENTRY_POINT + " --command register --port 9050 --gpio 2")
    print(" sudo " + ENTRY_POINT + " --command listen --port 9050 --gpio 2")
    if len(list_installed(PACKAGENAME)) > 0:
        print("example command s for registered services")
        for service_info in list_installed(PACKAGENAME):
            port = service_info[1]
            is_active = service_info[2]
            print(" sudo " + ENTRY_POINT + " --command log --port " + port)
            if is_active:
                print(" sudo " + ENTRY_POINT + " --command deregister --port " + port)



def main():
    parser = argparse.ArgumentParser(description='A web connected humidity and temperature sensor')
    parser.add_argument('--command', metavar='command', required=False, type=str, help='the command. supported commands are: listen (run the webthing service), register (register and starts the webthing service as a systemd unit, deregister (deregisters the systemd unit), log (prints the log)')
    parser.add_argument('--port', metavar='port', required=False, type=int, help='the port of the webthing serivce')
    parser.add_argument('--gpio', metavar='gpio', required=False, type=int, help='the gpio number wired to the DHTxxx signal pin')
    args = parser.parse_args()

    if args.command is None:
        print_info()
    elif args.command == 'listen':
        if args.port is None:
            print("--port is mandatory")
        elif args.gpio is None:
            print("--gpio is mandatory")
        else:
            print("running " + PACKAGENAME + " on port " + str(args.port) + "/gpio " + str(args.gpio))
            run_server(args.port, args.gpio, DESCRIPTION)
    elif args.command == 'register':
        if args.port is None:
            print("--port is mandatory")
        elif args.gpio is None:
            print("--gpio is mandatory")
        else:
            print("register " + PACKAGENAME + "/" + args.name + " on port " + str(args.port) + "/gpio " + str(args.gpio) + " and starting it")
            register(PACKAGENAME, ENTRY_POINT, int(args.port))
    elif args.command == 'deregister':
        if args.port is None:
            print("--port is mandatory")
        else:
            print("deregister " + PACKAGENAME + "/" + args.name + " on port " + str(args.port))
            deregister(PACKAGENAME, int(args.port))
    elif args.command == 'log':
        if args.port is None:
            print("--port is mandatory")
        else:
            printlog(PACKAGENAME, int(args.port))
    else:
        print("unsupported command")
        print_info()


if __name__ == '__main__':
    log_level = os.environ.get("LOGLEVEL", "INFO")
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=log_level, datefmt='%Y-%m-%d %H:%M:%S')

    main()

