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
            return True
        else:
            return False
    
    def disconnectCar(car):
        print("Actuator status is : " + car.getActuatorStatus())
        if car.getActuatorStatus() == "Connected":
            car.setActuatorStatus("Not Connected")
            return True
        else:
            return False

    def sendData():
        with open("static/level.txt", "r") as f: 
            level = f.read()

        return level


    def receiveData(level):
        if level == "Easy":
            with open("static/statusEasy.txt", "r") as f: 
                level2 = f.read()
        elif level == "Medium":
            with open("static/statusMedium.txt", "r") as f: 
                level2 = f.read()
        else:
            with open("static/statusHard.txt", "r") as f: 
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
            #print("STOP !")
            return True
        else:
            #print("No obstacle. Continue moving")
            return False
        return


def testCase1():
    print("Test case 1:\n")
    newCar1 = car(sensorStatus="No obstacle", actuatorStatus="Not Connected", speed="0 m/s")
    carController.connectCar(newCar1)
    carController.sendData()
    carController.detectObstacle(newCar1)
    print("\n")

def testCase2():
    print("Test case 2:\n")
    newCar2 = car(sensorStatus="Obstacle", actuatorStatus="Connected", speed="1 m/s")
    carController.disconnectCar(newCar2)
    level = carController.sendData()
    carController.receiveData(level)
    carController.detectObstacle(newCar2)
    print("\n")

def testCase3():
    print("Test case 3:\n")
    newCar3 = car(sensorStatus="No obstacle", actuatorStatus="Connected", speed="0 m/s")
    print("Current car speed is: " + newCar3.getSpeed())
    newCar3.setSpeed("1 m/s")
    print("New car speed is : " + newCar3.getSpeed())
    print("\n")


testCase1()
testCase2()
testCase3()
