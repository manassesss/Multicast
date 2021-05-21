import socket
import sys
import struct
import netifaces as ni

multicast_group = '224.3.29.71'
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

##creating a list of IP to use to find the smaller IP
ip_list = []
# Receive/respond loop
while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(1024)
    del(ip_list[ip_list.index(address[0])])

    #setting the servers to send and to answer requisition
    multicast_group_servers = ('224.0.0.1', 10001)
    sockServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockServer.settimeout(0.2)
    ttl2 = struct.pack('b', 1)
    sockServer.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl2)
    try:
        #setting sockets
        sockServer.bind('', 10001)
        group_2 = socket.inet_aton(multicast_group_servers[0])
        mreq2 = struct.pack('4sL', group_2, socket.INADDR_ANY)
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
        ni.ifaddresses('enp0s3')
        ip = ni.ifaddresses('enp0s3')[ni.AF_INET][0]['addr']
        print('IP Address: ', ip)

        if(min(ip_list)==int(ip.replace(".",""))):
            #the answer of the requisition 
            answer = str(eval(data.decode()))
            sock.sendto(str.encode(answer), address) #sending the answer

        ip_list =[]

