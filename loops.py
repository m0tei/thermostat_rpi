from values import *
from changeFunctions import *
import time

def tempLoop():
	while(True):
		currentTemp = readTemp()
		if(currentMode == "day"):
			if(currentTemp <= dayTemp - 0.25):
				turnOn()
			else:
				if(currentTemp >= dayTemp + 0.25):
					turnOff()
		if(currentMode == "night"):
			if(currentTemp <= nightTemp - 0.25):
				turnOn()
			else:
				if(currentTemp >= nightTemp + 0.25):
					turnOff()
		if(currentMode == ""):
			turnOff()
		time.sleep(5)