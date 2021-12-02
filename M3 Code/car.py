from flask import Flask
from datetime import datetime
import re
import json
import sys

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")

class car():
    def __init__(self, sensorStatus, actuatorStatus, speed):
        self.sensorStatus = sensorStatus
        self.actuatorStatus = actuatorStatus
        self.speed = speed

    def getSensorStatus(self):
        return self.sensorStatus
    

    def getActuatorStatus(self):
        return self.actuatorStatus
    
    def setActuatorStatus(self, actuator):
        self.actuatorStatus = actuator
        return

    def getSpeed(self):
        return self.speed
    

    def setSpeed(self, speed):
        self.speed = speed
        return


class carController():
    def connectCar(car):
        print("Actuator status is : " + car.getActuatorStatus())
        if car.getActuatorStatus() == "Not Connected":
            car.setActuatorStatus("Connected")
        print("Actuator status is : " + car.getActuatorStatus())
        return
    
    def disconnectCar(car):
        print("Actuator status is : " + car.getActuatorStatus())
        if car.getActuatorStatus() == "Connected":
            car.setActuatorStatus("Not Connected")
        print("Actuator status is : " + car.getActuatorStatus())
        return

    def sendData():
        with open("static/level.txt", "r") as f: 
            level = f.read()

        return level


    def receiveData():
        with open("static/status.txt", "r") as f: 
            level2 = f.read()
            split = level2.split("-")
            sensor = split[0]
            dist = split[1]
            speed = split[2]
            actuator = split[3]
        data = [sensor, dist, speed, actuator]

        return data

    def detectObstacle(car):
        print("Sensor status is : " + car.getSensorStatus())
        if car.getSensorStatus() == "Obstacle":
            print("STOP !")
        return


def testCase1():
    print("Test case 1:\n")
    newCar1 = car(sensorStatus="Obstacle", actuatorStatus="Not Connected", speed="0 m/s")
    carController.disconnectCar(newCar1)
    carController.connectCar(newCar1)
    carController.sendData()
    carController.receiveData()
    carController.detectObstacle(newCar1)
    print("\n")

def testCase2():
    print("Test case 2:\n")
    newCar2 = car(sensorStatus="No Obstacle", actuatorStatus="Connected", speed="0 m/s")
    carController.disconnectCar(newCar2)
    carController.connectCar(newCar2)
    carController.sendData()
    carController.receiveData()
    carController.detectObstacle(newCar2)
    print("\n")


testCase1()
testCase2()
