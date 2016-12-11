#!/usr/bin/python
from socket import *
from thread import *
import json
import sys
 
class key_store_server:

	def __init__(self,no_of_versions) :
		self.n = no_of_versions # set the number of versions 
		host = gethostname()
		port = 777 
 
		self.sock = socket() # start a socket
		self.sock.bind((host, port))

		self.sock.listen(2000) 
 
	def handle_client(self,conn):
		print "Listening from a new client"
		conn.send("Connected to server!\n To add use syntax ADD k1 v1\nTo get key use GET key\n   or\nGET 1 version1\nTo delete a key use DELETE key")
		while True:
			data = conn.recv(1024)  # recvieve from client
			print "Recieved : ",data
			data = data.split()
			if len(data) > 0 :
				with open('key_store.json','r') as read_json :
					file = read_json.read() # read the data stored in json
					json_data = {}
					if len(file) > 0 :
						json_data = json.loads(file)
					if data[0].upper() == "ADD" and len(data) == 3 : # to add
						key = data[1]
						value = data[2]
						if json_data.has_key(key) and len(json_data[key]) == self.n : # if the number of versions for a key is == n. then pop and insert.
							json_data[key].pop()
							json_data[key].insert(0,value)
						elif not json_data.has_key(key) :  # if key has no versions
							json_data[key] = [value]
						else :
							json_data[key].insert(0,value) # insert at first
						with open('key_store.json','w') as write_json : # write into file
							write_json.write(json.dumps(json_data))
							conn.send("inserted successfully")
						
					elif data[0].upper() == "GET" : # get version
						key = data[1]
						print key
						if len(data) == 2 :
							if json_data.has_key(key) : # return latest installed version
								conn.send(str(json_data[key][0]))
							else :
								conn.send("invalid key")
						elif len(data) == 3 :
							version = int(data[2])
							print key,version
							
							if json_data.has_key(key) and version > 0 and version < self.n:
								conn.send(str(json_data[key][version]))
							else :
								conn.send("invalid key")
					
					elif data[0].upper() == "DELETE" : # delete entire key
						key = data[1]
						if json_data.has_key(key) :
							del json_data[key]
							with open('key_store.json','w') as write_json :
								write_json.write(json.dumps(json_data))
								conn.send("Delete succesfully")
						else :
							conn.send("Inavlid key")
							
						
					else :
						conn.send("Invalid syntax or value")
							
					
				
				
		 
 
	def start_server(self):
		print "**************** Started Server ********************"
		while True:
			conn, addr = self.sock.accept() # accept a new connection from a new client
			start_new_thread(self.handle_client,(conn,)) # start a new thread to handle new client connection
		conn.close()
		self.sock.close()
		
if __name__ == "__main__" :
	if len(sys.argv) < 2 :
		print "Please run programm with version size as command line argument like this\n    python key_store_server.py n"
	else :
		n = int(sys.argv[1])
		key_store_server(n).start_server() # instantiate and start server