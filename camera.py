""
#This is the camera class 
""
class camera:

    def __init__(self, resolution, zoom, nightvision, hasflash) -> None:
        self._resolution = resolution #self. makes it an attribute
        self._zoom = zoom # _zoom says location should be private
        self._nightvision = "#nightvision"
        self._hasflash = "#hasflash"

        def  TurnOn(self):
             print("Turn the Camera on")

        ""
        #Method to make camera turn on and off to capture photo
        ""
        def TurnOff(self):
            print("Turn the Camera off")   
