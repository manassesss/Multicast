import socket
import sys
import struct



try:
    exp = input('Put the expression: ')
except:
    print("INVALID EXPRESSION")

multicast_group = ('224.3.29.1', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.timeout(5)
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:

    print('sending "%s"' % exp)
    sent = sock.sendto(str.encode(exp), multicast_group)
    while True:
        print('waiting to receive...')    
        try:
            
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('time out, no more responses')
            break
        else:
            print('received "%s" from "%s"' % (data, server))

finally:
    print('closing socket')
    sock.close()
