""" Supplied camera module"""

import os
from PIL import Image


class Camera():
    """
    Uses RasPi camera to take a picture and save.
    """
    def __init__(self, img_width=128, img_height=96, img_rot=0, filetype="png"):
        self.value = None
        self.filetype = str(filetype)
        self.img_width = img_width
        self.img_height = img_height
        self.img_rot = img_rot

    def get_value(self):
        """Getter for value"""
        return self.value

    def update(self):
        """Update"""
        self.sensor_get_value()
        return self.value

    def reset(self):
        """Reset"""
        self.value = None

    def sensor_get_value(self):
        # This is a OS call that takes a image and makes it accessible to PIL
        # operations in the same directory
        os.system('raspistill -ss 6000 -o project6_supply/sensors/image.' + self.filetype + ' -w "' + str(self.img_width) +
                  '" -h "' + str(self.img_height) + '" -rot "' + str(self.img_rot) + '"')
        # Open the image just taken by raspicam
        # Stores the RGB array in the value field
        self.value = Image.open('project6_supply/sensors/image.png').convert('RGB')

# Just testing the camera in python

# os.system('raspistill -t 1 -o image.png -w "' + str(200) + '" -h "' +
# str(200) + '" -rot "' + str(0) + '"')
