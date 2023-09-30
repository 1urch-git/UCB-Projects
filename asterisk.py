import socket


#Initiate the connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(('159.223.206.129',8002))
data = s.recv(1024)

"""
STAGE 1
"""
#Send precalculated numbers
s.send('16\r\n'.encode())
s.send('65536\r\n'.encode())
s.send('4194304\r\n'.encode())
print("STAGE 1 COMPLETE")

"""
STAGE 2
"""

#Stage 2 = receive additional questions to solve
data = s.recv(1024)
data = s.recv(1024)
data = s.recv(1024)
data = s.recv(1024)

stage2 = s.recv(1024).decode()
#capture the values, perform addition, send solutions
expressions = stage2.split(">")
operation1 = expressions[1].split('+')
operation2 = expressions[2].split('+')
operation3 = expressions[3].split('+')
num1 = operation1[0].strip()
num2 = operation1[1].strip()
num3 = operation2[0].strip()
num4 = operation2[1].strip()
num5 = operation3[0].strip()
num6 = operation3[1].strip()
#Clean up the numbers of non-numeric characters before bundling to send back

#perform addition operations on numbers
response1 = str(int(num1)+int(num2))
response2 = str(int(num3)+int(num4))
response3 = str(int(num5)+int(num6))

#send responses
s.send((response1+'\r\n').encode())
s.send((response2+'\r\n').encode())
s.send((response3+'\r\n').encode())
data = s.recv(1024)
#print(data) #flag 2
print("STAGE 2 COMPLETE")

"""
STAGE 3
"""
data = s.recv(1024)
data = s.recv(1024)
data = s.recv(1024)
data = s.recv(1024)

def stripper():
	print("starting stripper 1")
	end = False #this is currently doing nothing
	numbers = []
	#continue to receive data until the line break is reached
	while end == False:
		data = s.recv(1024).decode()
		#print(data)
		if "\n" in data:
			end = True #terminate loop
			
		
		if "+" in data:
			divider = data.split("+")
			numbers.append(divider[0])
			_1stnumber = numbers
			numbers = []
			numbers.append(divider[1])
		else:
			numbers.append(data)

	def numextract(mylist):
		newlist = []
		for text in mylist:
			for j in text:
				if j.isdigit():
					newlist.append(j)

		number = ''
		for digit in newlist:
			number += digit
		return(int(number))

	numberone = numextract(_1stnumber)
	numbertwo = numextract(numbers)
	response = numberone+numbertwo
	s.send((str(response)+"\r\n").encode())

	"""print("number one: ", numberone)
	print("number two: ", numbertwo)
	print(response)"""
stripper()

    

#Second operation of stage 3, which begins and ends with line break
#as such, we need to modify the above function
def stripper2():
	print("starting stripper2...")
	data = s.recv(1024).decode() #delivers the 2nd operation of form \n> ### + ### \n
	#print(data)

	numbers= []  
	
	if "+" in data:
		divider = data.split("+")
		numbers.append(divider[0])
		_1stnumber = numbers
		numbers = []
		numbers.append(divider[1])
	else:
		numbers.append(data)

	#print(_1stnumber, numbers)
	
	def numextract(mylist):
		newlist = []
		for text in mylist:
			text = text.strip()
			for j in text:
				if j.isdigit():
					newlist.append(j)
		#print(newlist)
		number = ''
		for digit in newlist:
			number += digit
		#print(number)
		return(int(number))
	
	numberone = numextract(_1stnumber)
	numbertwo = numextract(numbers)
	response = numberone+numbertwo

	#print("number one: ", numberone)
	#print("number two: ", numbertwo)
	#print(response)

	s.send((str(response)+"\r\n").encode())


stripper2()
stripper2()

def stripper3(): #first several characters are endian format, need to add another split in divider
	print("starting stripper3...")
	data = s.recv(1024).decode() #delivers the 3rd operation of form \xab\xab\xab ### + ### \n
	#print(data)

	numbers= []  
	
	if "+" in data:
		divider = data.split("+")
		beginning = divider[0].split(" ")
		numbers.append(beginning[1])
		_1stnumber = numbers
		numbers = []
		numbers.append(divider[1])
	else:
		numbers.append(data)

	#print(_1stnumber, numbers)
	
	def numextract(mylist):
		newlist = []
		for text in mylist:
			text = text.strip()
			for j in text:
				if j.isdigit():
					newlist.append(j)
		#print(newlist)
		number = ''
		for digit in newlist:
			number += digit
		#print(number)
		return(int(number))
	
	numberone = numextract(_1stnumber)
	numbertwo = numextract(numbers)
	response = numberone+numbertwo

	#print("number one: ", numberone)
	#print("number two: ", numbertwo)
	#print(response)

	s.send((str(response)+"\r\n").encode())
stripper3() #run the funciton
data = s.recv(1024) #receive the final flag
print(data)

print("STAGE 3 COMPLETE")

s.close() #close the connection
