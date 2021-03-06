import socket
import sys
import struct
#import netifaces as ni

multicast_group = '224.3.29.1'
server_address = ('', 10000)
multicast_group_servers = ('224.0.0.1', 10001)
# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Getting the name of the host
ip = socket.gethostbyname(socket.gethostbyname())
# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

##creating a list of IP to use to find the smaller IP
ip_list = ['1010101', '1010102', '1010103', '1010104']

# Receive/respond loop
while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(1024)
    try:
        del(ip_list[ip_list.index(address[0].replace(".",""))])
    except:
        pass

    #setting the servers to send and to answer requisition
    sockServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockServer.settimeout(0.2)
    ttl2 = struct.pack('b', 1)
    sockServer.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl2)
    try:
        #setting sockets
        sockServer.bind(('', 10001))
        #group_2 = socket.inet_aton(multicast_group_servers[0])
        mreq2 = struct.pack('4sL', group, socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq2)

        #sending a message among the servers
        sockServer.sendto(b'online', multicast_group_servers)

        while True:
            print('\nwaiting to receive response from servers')
            try:
                data2, addressServer = sockServer.recvfrom(1024)
            except socket.timeout:
                print('time out, no mores answers!')
                break
            else:
                print('received %s  from %s' % (data, address))
    finally:
        sockServer.close()
        
        #finding the server IP
        #ni.ifaddresses('eth0s')
        #ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        print('IP Address: ', ip)

        if(min(ip_list)==int(addressServer[0].replace(".",""))):
        #the answer of the requisition 
            answer = str(eval(data))
            sock.sendto(str.encode(answer), address) #sending the answer

