class radio:
    #class variables
    color="Blue"
    brand="Oneplus"
    ACPower=False
    headphone=False
    #Constructor
    def __init__(self):
        self.led=None
        self.Mode=None
        self.freq=0.0
        self.Vol=0
        print("Your Radio is ready to be played.")
        
    #Instance method to switch on power.
    def SwitchPower(self,pow):
        self.ACPower=pow
        print('Your radio is powered '+str(self.ACPower))        
        
    #Instance method to check presence of headphone jack
    def checkJack(self,HP):
        self.headphone=HP
        print('Your Radio has a headphone jack: '+str(self.headphone))   
        
    #Instance method to check if power led is working or not
    def PowLed(self,pLed):
        self.led=pLed
        print('Your radio\'s power led is '+str(self.led))        
        
    #Instance method to check which mode is you radio switched to    
    def CheckMode(self,M):
        self.Mode=M
        print('Your radio\'s MOde is turned to '+str(self.Mode))    
        
    #Instance method to get the freuency value for your radio station
    def getFreq(self,F):
        self.freq=F
        print('you radio is catching frequency of value '+str(self.freq))        
        
    #Instance method to get the required volume for the listener
    def vol(self,V):
        self.Vol=V
        print('the volume of your radio is set to '+str(self.Vol))        
        
#Create the Instance of class radio
R1= radio()
print('Color of your radio is '+str(radio.color))  
print('Brand of your radio is '+str(radio.brand))

R1.SwitchPower("ON")

R1.checkJack(False)

R1.PowLed("ON")

R1.CheckMode("FM")

R1.getFreq(109.0)

R1.vol(9)

print('Listen to your favourite song')

#after listening switch of the radio
R1.SwitchPower("OFF")

#destroy the radio
R1=None
