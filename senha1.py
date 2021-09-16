
import string,random
ram =[]
for i in range(10000):
	senha = ''
	for i in range(10):
		senha+= random.choice(string.digits+' ')
	if not senha in ram:
		ram.append(senha)
		print(senha)






