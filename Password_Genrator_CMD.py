import random

def genrator(n):
	global schar,cchar
	schar = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
	cchar = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
	num = [1,2,3,4,5,6,7,8,9,0]
	symb = ['~','`','!','@','/#','$','%','^','&','*']
	pass_size = n
	paswd = " "
	for i in range (1,pass_size+1):
		ran1= [schar,cchar,num,symb]
		ran1_choice = random.choice(ran1)
		ran2 = random.choice(ran1_choice)
		paswd += str(ran2)
	print("Your Password : ",paswd)
	
try:	
	n = input("Enter the Size of Password you wanted: ")	
	n = int(n)
	genrator(n)
except ValueError:
	print ("Only enter numerical value")

