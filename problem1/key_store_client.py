import socket
soc = socket.socket()
soc.connect((socket.gethostname(),777))
print soc.recv(1024)
print "0 to exit client"
while True :
	inp = raw_input()
	if inp == "0" :
		break
	soc.send(inp)
	print "Response from server : ",soc.recv(1024)
