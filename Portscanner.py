import socket
import Ports

ip = input("Wybierz swój cel: ")

for port in range(1, 1025):
    s = socket.socket()
    s.settimeout(0.125)
    result = s.connect_ex((ip, port))
    if result == 0:
        portName = Ports.WELL_KNOW_PORTS[port]
        print(f"Port {port} {portName} jest otwary")

    s.close()
print("Skanowanie portów zakończone")

