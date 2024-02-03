import socket
from _thread import * # this is for threading

server = "172.16.96.243"
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
    
    reply = ""
    while True:
        try:
            data = conn.recv(2048) # how much data do you want to receive
            reply = data.decode("utf-8")
            
            if not data:
                print("Disconnected")
                break
            else:
                print("Received:", reply)
                print("Sending:", reply)
                
            conn.sendall(str.encode(reply)) #encoding the data before sending it
        except:
            break;
            
        
while True:
    conn, addr = s.accept() # conn is the connection, addr is the ip address
    print("Connected to:", addr)
    
    start_new_thread(threaded_clients, (conn,))  

