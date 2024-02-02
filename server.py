import socket
from _thread import * # this is for threading

server = ""
port = 5555

# these are types of connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)
    
s.listen(2) # how many clients (listeners) do you 
            # want to let connect to your server
print("Waiting for a connection, Server Started")

def threaded_clients(conn):
    pass

while True:
    conn, addr = s.accept() # conn is the connection, addr is the ip address
    print("Connected to:", addr)
    
    start_new_thread(threaded_clients, (conn,))  

