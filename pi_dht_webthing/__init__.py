
import argparse
from pi_dht_webthing.dht_webthing import run_server
from pi_dht_webthing.unit import register, deregister, printlog


def main():
    parser = argparse.ArgumentParser(description='A web connected humidity and temperature sensor')
    parser.add_argument('--command', metavar='command', required=True, type=str, help='the command. supported commands are: listen (run the webthing service), register (register and starts the webthing service as a systemd unit, deregister (deregisters the systemd unit), log (prints the log)')
    parser.add_argument('--port', metavar='port', required=True, type=int, help='the port of the webthing serivce')
    parser.add_argument('--gpio', metavar='gpio', required=False, type=int, help='the gpio number wired to the DHTxxx signal pin')
    args = parser.parse_args()

    if args.command == 'listen':
        print("running dht webthing on port " + str(args.port) + "/gpio " + str(args.gpio))
        run_server(args.port, args.gpio)
    elif args.command == 'register':
        print("register dht webthing service on port " + str(args.port) + "/gpio " + str(args.gpio) + " and starting it")
        register('pi_dht_webthing', int(args.port), int(args.gpio))
    elif args.command == 'deregister':
        print("deregister dht webthing service on port " + str(args.port))
        deregister('pi_dht_webthing', int(args.port))
    elif args.command == 'log':
        printlog('pi_dht_webthing', int(args.port))
    else:
        print("usage dht --help")


if __name__ == '__main__':
    main()

