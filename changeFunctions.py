from values import *

def readTemp():
	return 21

def turnOn():
	print("turnOn")

def turnOff():
	print("turnOff")

def changeMode(mode):
	global currentMode
	currentMode = mode

def changeDayTemp(temp):
	global dayTemp
	dayTemp = dayTemp

def changeNightTemp(temp):
	global nightTemp
	nightTemp = temp

	