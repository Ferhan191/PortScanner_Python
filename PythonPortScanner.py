import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = input("Enter ip address ")

while True:
    port = int(input("Enter port address "))

    def portScanner(port):
        if s.connect_ex((host,port)):
            print("{} port is closed".format(port))
        else:
            print("{} port is opening".format(port))

    portScanner(port);
    print("")
