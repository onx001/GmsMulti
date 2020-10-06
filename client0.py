import socket

UDP_IP = "35.212.254.154"
#UDP_IP = "10.56.57.143"
UDP_PORT = 5070
MESSAGE = b"Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print(data)
    sock.sendto(b"close", (UDP_IP, UDP_PORT))
