import socket
import time

host = "127.0.0.1"
port = 5000
users = []

#We will be using UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)
print("Server started at" + time.ctime(time.time()))
quit = False
while not quit:
    try:
        data, addr = s.recvfrom(1024)
        print("-------------")

        if addr not in users:
            users.append(addr)
            print("joined: "+str(addr[1]))

        print(time.ctime(time.time()) + str(data))
        for user in users:
            s.sendto(data, user)
    except:
        time.sleep(0.1)
s.close()
