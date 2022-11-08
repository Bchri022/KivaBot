"""
File: #containing Sensors and MotionSensor classes
""" 
class #sensors:
    def __init__(self, resolution, zoom, night vision, has flash) -> None:
        self._redlight = "redlight" #self. makes it an attribute
        self._shape = "shape" # _shape says location should be private
        self._weight = "weight"
       

        def  TurnFlashingOn(self):
             print("Turn the Flashing  on")

        """
        #Method to make robot flash on when object is in it's way and flash off when removed out of way
        """
        def TurnFlashingOff(self):
            print("Turn Flashing off")
        
        """"
        MotionSensor is a subclass of Sensors
        """
class #MotionSensor("Sensors"):
    def __init__(self, weight, size) -> None:
        super().__init__(weight, size)
        self._Flashingbrightness= 0
        
        def  setFlashingBrightness(self):
             print("fSet the Flashing Brightness to a level {level}")
             self._flashingbrightness = "level" 

       