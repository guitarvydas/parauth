class Lamp:
    def __init__ (self):
        self.on = False
        self.intensity = "low"

    def pwr (self):
        if self.on:
            self.powerOff ()
        else:
            self.powerOn ()

    def powerOn (self):
        self.on = True
        self.intensity = "low"
        self.printState ()

    def powerOff (self):
        self.on = False
        self.printState ()

    def printState (self):
        if self.on:
            print (f'on, {self.intensity}')
        else:
            print ('off')

    def toggleIntensity (self):
        if self.intensity == "low":
            self.intensity = "medium"
        elif self.intensity == "medium":
            self.intensity = "high"
        else:
            self.intensity = "low"
        self.printState ()

class LampBad (Lamp):
    def __init__ (self):
        super ().__init__ ()
                  
    def pwr (self):
        if not self.on:
            self.powerOn ()
            self.intensitey = "high"
        elif self.on and self.intensity == "low":
            self.powerOff ()
        else:
            self.toggleIntensity ()
            
print ("basic lamp")
lamp = Lamp ()
lamp.pwr ()
lamp.toggleIntensity ()
lamp.toggleIntensity ()
lamp.pwr ()
lamp.pwr ()

print ("\ninherited lamp")
blamp = LampBad ()
blamp.pwr ()
blamp.toggleIntensity ()
blamp.toggleIntensity ()
blamp.pwr ()
blamp.pwr ()

