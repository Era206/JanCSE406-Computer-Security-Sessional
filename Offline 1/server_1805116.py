from encryption_serverside_1805116 import *
from diffie_hellman_serverside_1805116 import *
from integer_to_character_string_1805116 import *
# first of all import the socket library
import socket            
 
# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")           
 
# a forever loop until we interrupt it or
# an error occurs
while True:
 
    # Establish connection with client.

    c, addr = s.accept()  
    size=128
    p,g,A,a=key_generation_for_sender(size)
    print ('Got connection from', addr )    
    
    # send a thank you message to the client. encoding to send byte type.
    c.send('Thank you for connecting '.encode())
    data = str(p) + ',' + str(g) + ',' + str(A) + ',' + str(size)
    c.sendall(data.encode('utf-8'))
    data = c.recv(1024).decode('utf-8')
    B = int(data)
    secret_key_int=secret_key_generation_server(p,a,B)
    secret_key_string=get_int_to_char_string(secret_key_int, size)
    print(' ')
    print("secret key: "+secret_key_string)
    print("plain text: "+ plainText)
    encrypted_char_string=encryption(secret_key_string)
    data=encrypted_char_string
    print("cipher text: "+data)
    c.sendall(data.encode('utf-8'))
    # Close the connection with the client
    c.close()
    
    # Breaking once connection closed
    break