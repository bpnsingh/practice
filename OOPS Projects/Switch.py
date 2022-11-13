class LightSwitch:
    def __init__(self):
        self.switchIson = False
    def turnOn(self):
        self.switchIson = True
    def turnOff(self):
        self.switchIson = False
    def show(self):
        print(self.switchIson)

oswitch1 = LightSwitch()
oswitch1.show()
oswitch1.turnOn()
oswitch1.show()
oswitch1.turnOff()
oswitch1.show()
