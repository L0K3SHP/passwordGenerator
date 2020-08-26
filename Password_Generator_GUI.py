import tkinter
from tkinter import *
import random

def genrator(password,display):
	schar = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
	cchar = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
	num = [1,2,3,4,5,6,7,8,9,0]
	symb = ['~','`','!','@','/#','$','%','^','&','*']
	pass_size = random.randint(10,17)
	paswd = " "
	for i in range (1,pass_size+1):
		ran1= [schar,cchar,num,symb]
		ran1_choice = random.choice(ran1)
		ran2 = random.choice(ran1_choice)
		paswd += str(ran2)
	display.config(text="Your Password")
	password.delete(0, END)
	password.insert(0,paswd)

while True :
	root = tkinter.Tk()
	root.title("Password Genrator")	
	root.geometry("500x100")
	header= Label(root,text="Password Genrator")
	header.place(x=350,y=500)
	password = Entry(root,text=" ")
	display = Label(root)
	display.place(x=410,y=750)
	genrate = Button(root,text="Genrate",					command=genrator(password,display))
	genrate.place (x=410,y=600)
	password.place(x=270,y=900)
	root.mainloop()