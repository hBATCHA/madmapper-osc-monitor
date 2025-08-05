from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

def print_handler(address, *args):
    print(f"📡 Reçu OSC: {address} -> {args}")

dispatcher = Dispatcher()
dispatcher.set_default_handler(print_handler)

ip = "127.0.0.1"
port = 7000

server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)

print(f"👂 En écoute sur {ip}:{port} (intercepte les messages du Manager vers MadMapper)")
print("Appuie sur Ctrl+C pour arrêter.")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\n🛑 Arrêt manuel.")
