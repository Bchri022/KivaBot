""
#This is the camera class 
""
class Camera:

    def __init__(self, resolution, zoom, night vision, has flash) -> None:
        self._resolution = resolution #self. makes it an attribute
        self._zoom = zoom # _zoom says location should be private
        self._nightvision = "#nightvision"
        self._hasflash = "#hasflash"

        def  TurnOn(self):
             print("Turn the Camera on")

        ""
        #Method to make camera turn on and off to capture photo
        ""
        def go(self):
            print("Turn the Camera off")   