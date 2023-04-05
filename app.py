from flask import Flask
import threading
from changeFunctions import *
from loops import *


app = Flask(__name__)

@app.route("/changeMode/<mode>")
def Mode(mode):
    changeMode(mode)

@app.route("/changeDayTemp/<temp>")
def DayTemp(temp):
    changeDayTemp(temp)

@app.route("/changeNightTemp/<temp>")
def NightTemp(temp):
    changeNightTemp(temp)

tempLoop = threading.Thread(target=tempLoop)
tempLoop.start() 

if __name__ == '__main__':
   app.run()
