import socket

ip = input("Wybierz swój cel: ")

for port in range(1, 1025):
    s = socket.socket()
    s.settimeout(0.125)
    result = s.connect_ex((ip, port))
    if
    if result == 0:
        print(f"Port {port} jest otwary")

    s.close()
    print("Skanowanie portów zakończone")

