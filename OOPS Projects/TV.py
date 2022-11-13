class TV:
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        self.channelList = [2,4,5,7,9,11,20,36,44,54,65]
        self.nchannels = len(self.channelList)
        self.chanelIndex = 0
        self.VOLUME_MIN = 0
        self.VOLUME_MAX = 10
        self.volume = self.VOLUME_MAX

    def power(self):
        self.isOn = not self.isOn

    def volumeUp(self):
        if not self.isOn :
            return
        if self.isMuted :
            self.isMuted = True
        if self.volume < 10:
            self.volume += 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = True
        if self.volume > 0:
            self.volume -= 1

    def channelUp(self):
        if not self.isOn :
            return
        self.chanelIndex += 1
        if self.chanelIndex > self.nchannels:
            self.chanelIndex = 0
    def channelDown(self):
        if not self.isOn:
            return
        self.chanelIndex = self.chanelIndex -1
        if self.chanelIndex < 0:
            self.chanelIndex = self.nchannels -1

    def mute(self):
        if not self.isOn :
            return
        self.isMuted = not self.isMuted

    def setChannel(self,newChannel):
        if newChannel in self.channelList:
            self.chanelIndex = self.channelList.index(newChannel)

    def showInfo(self):
        print()
        print("TV Status")
        if self.isOn :
            print ("    TV is ON")
            print("{0}  Channel number".format(self.channelList[self.chanelIndex]))
            if self.isMuted :
                print ("TV is Muted")
            else:
                print ("Volume is {}".format(self.volume))
        else:
            print("TV is off")


oTV = TV()  # create the TV object

# Turn the TV on and show the status
oTV.power()
oTV.showInfo()

# Change the channel up twice, raise the volume twice, show status
oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

# Turn the TV off, show status, turn the TV on, show status
oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

# Lower the volume, mute the sound, show status
oTV.volumeDown()
oTV.mute()
oTV.showInfo()

# Change the channel to 11, mute the sound, show status
oTV.setChannel(11)
oTV.mute()
oTV.showInfo()










