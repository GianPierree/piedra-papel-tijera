#!/usr/bin/python
#!/usr/bin/env python
# -*-coding:utf-8-*-
import Tkinter, tkSimpleDialog
import time
from time import sleep
import random
root = Tkinter.Tk()
root.withdraw()
sus = "-"*35
depo = ["piedra","papel","tijera"]
while True:
	#x = raw_input("Que elijes? piedra, papel o tijera: ")
	x = tkSimpleDialog.askstring("String", "Que elijes? piedra, papel o tijera:")
	if x not in depo:
		print("No hagas trampa!!!")
		continue
	pc = random.choice(depo)
	sleep(0.5)
	print(("computadora elijio {}.").format(pc))
	if x==pc:
 		print "\nEmpate."
	elif x=="piedra" and pc=="tijera":
		print "\nGanaste"
	elif x=="papel" and pc=="piedra":
		print "\nGanaste"
	elif x=="tijera" and pc=="papel":
		print "\nGanaste"
	else:
		print "perdimos. {} gana {} \n".format(pc, x)
	print sus