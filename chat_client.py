import socket
import threading
import time

tlock = threading.Lock()
exit = False
host = "127.0.0.1"
port = 0

def message_recieve(name, sock):
    while not exit:
        try:
            tlock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print("... " + str(data.decode('ascii')))
        except:
            pass
        finally:
            tlock.release()


server = ("127.0.0.1", 5000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)
rt = threading.Thread(target=message_recieve, args=('Thread', s))
rt.start()

alias = input("Your nickname: ")
print("Hi " + alias + " welcome to the chat!")
print("-----------------------------")
message = input(alias + "-> ")
while str(message) != "q":
    if str(message) != "":
        s.sendto(alias.encode('ascii') + ": ".encode('ascii') + message.encode('ascii'), server)
    tlock.acquire()
    message = input(alias + "-> ")
    tlock.release()
    time.sleep(0.2)

exit = True
rt.join()
s.close()
