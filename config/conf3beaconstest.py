#
#
# configuration file - contains customization for exact system
# SDL December 2020
#

serverURL = "http://192.168.1.40"

DEBUG = True

LIGHT_BRIGHTNESS_SENSITIVITY = 2.0
LIGHT_DISTANCE_SENSITIVITY = 2.0
# configuration for house
# list of iBeacons with x,y coordinates.  Top left corner of image is 0,0
# list of lists
# Beacon format:
#     BeaconNumber, LocalName, x, y, UDID, Major, Minor, Measured Power (from spec), x in px, y in px
# BeaconNumber is incremental from 0 up.  Don't skip a number

#pix converter

def pixelConv(pixels):
	return round(pixels * 0.0375,2)    # in meters

def meterToPixel(meters):
	return int(meters / 0.0375)    # in pixels 

BeaconList=[]
BeaconCount = 0

Beacon = [BeaconCount,"BlueCharm #0 Beacon", pixelConv(0), pixelConv(0),  "dd:33:0a:11:19:cb", 3838, 4949, -64, 314, 507]
BeaconList.append(Beacon)
BeaconCount += 1

Beacon = [BeaconCount,"BlueCharm #1 Beacon", pixelConv(100), pixelConv(0),  "dd:33:0a:11:1b:2f", 28849,11936, -64, 137, 36]
BeaconList.append(Beacon)
BeaconCount += 1

Beacon = [BeaconCount,"BlueCharm #2 Beacon", pixelConv(0), pixelConv(100),  "dd:33:0a:11:19:c0", 28849,11936, -64, 137, 36]
BeaconList.append(Beacon)
BeaconCount += 1



# transform

for beacon in BeaconList:
	beacon[4] = beacon[4].replace(" ", "")
	beacon[4] = beacon[4].replace("-", "")
	beacon[4] = beacon[4].upper()


#list of lights
#Light Format
#     LightNumber, LocalName, x, y, pixel x, pixel y, light on/off (1/0), huelightnumber 

hue = 0
LightList=[]
LightCount = 0
Light = [LightCount, "Lab desk", pixelConv(0), pixelConv(0),0, 0,1, 25] 
LightList.append(Light)
LightCount += 1



