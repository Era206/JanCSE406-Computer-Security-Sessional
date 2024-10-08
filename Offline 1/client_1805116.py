from decryption_client_side_1805116 import *
from diffie_hellman_clientside_1805116 import *
from integer_to_character_string_1805116 import *
# Import socket module
import socket			

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 12345			

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
print(' ')
data = s.recv(1024).decode('utf-8')
p, g, A, size = data.split(',')
p, g, A ,size= int(p), int(g), int(A),int(size)
B,b=key_generation_for_sender(size,g,p)
secret_key_int=secret_key_generation_client(p,b,A)
secret_key_string=get_int_to_char_string(secret_key_int,size)

print("secret key: "+secret_key_string)
data = str(B) 
s.sendall(data.encode('utf-8'))
encrypted_text=s.recv(1024).decode('utf-8')
print("cipher text: "+encrypted_text)
decrypted_text=decryption(encrypted_text,secret_key_string)
print("deciphered text: "+decrypted_text)
# close the connection
s.close()	
	
