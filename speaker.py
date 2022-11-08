""
#This is the speaker class 
""
class Speaker:

    def __init__(self, audio, volume,) -> None:
        self._audio = audio #self. makes it an attribute
        self._volume = volume 
        
        def  IncrementVolumeOn(self):
             print("Turn the Volume up")

        ""
        #Method to make speaker go higher or lower
        ""
        def DecrementVolumeOff(self):
            print("Turn the Volume down")