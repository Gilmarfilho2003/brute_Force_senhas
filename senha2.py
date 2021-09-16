import string,random
ram =[]
for i in range(10000000000000000000000000000000000):
	senha = ''
	for i in range(6):
		senha+= random.choice(string.ascii_letters+' ')
	if not senha in ram:
		ram.append(senha)
		print(senha)
 
