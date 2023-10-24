import socket
import re

target_host = "159.223.206.129"
target_port = 8005
for i in range (100):
	#create socket object
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#connect to client
	client.connect((target_host,target_port))

	#send data
	client.send(b"GET /flag.txt HTTP/1.1\r\nHost: cyber210.network\r\n\r\n")

	#receive data
	response = client.recv(4096)

	response = response.decode()
	#print(response)

	ham = bool(re.search("Ham", response))
	if ham == True:
		print(response)

client.close()

