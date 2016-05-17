
import socket
import sys
host =' '
port = 1997


s=socket.socket(socket.AF_INET , SOCKET.SOCK_STREAM)
host=socket.gethostname()

s.connect((host,port))
msg='hello?'

try :
	s.sendall(msg)
except:
	socket.error 
	print 'msg sending failed'
	sys.exit
print 'msg sent'


s.getting(10)
print 'socket now listening and getting'




def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1992)
        reply = 'OK...' + data
        if not data: 
            break
     
        conn.sendall(reply)
     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()






reply=s.recieve(1992)
print reply
s.close()


