#
#
# configuration file - contains customization for exact system
# SwitchDoc Labs 2020 
#
serverURL = "http://example.example.com:9600"

DEBUG = True

LIGHT_BRIGHTNESS_SENSITIVITY = 2.0
LIGHT_DISTANCE_SENSITIVITY = 2.0
# configuration for house
# list of iBeacons with x,y coordinates.  Top left corner of image is 0,0
# list of lists
# Beacon format:
#     BeaconNumber, LocalName, x, y, MAC, Major, Minor, Measured Power (from spec), x in px, y in px
# BeaconNumber is incremental from 0 up.  Don't skip a number

#pix converter

def pixelConv(pixels):
	return pixels * 0.0375    # in meters

def meterToPixel(meters):
	return int(meters / 0.0375)    # in pixels 

BeaconList=[]
BeaconCount = 0

Beacon = [BeaconCount,"Estimote #0 Beacon", pixelConv(314), pixelConv(507),  "43:ed:21:ac:77:ed", 64507, 5414, -64, 314, 507]
BeaconList.append(Beacon)
BeaconCount += 1

Beacon = [BeaconCount,"Estimote #1 Beacon", pixelConv(110), pixelConv(36),  "53:1f:e6:22:6c:0c", 28849,11936, -64, 137, 36]
BeaconList.append(Beacon)
BeaconCount += 1

Beacon = [BeaconCount,"Estimote #2 Beacon", pixelConv(137), pixelConv(144),  "f8:04:2e:bf:d2:05", 56124, 58492, -64, 137, 144]
BeaconList.append(Beacon)
BeaconCount += 1

Beacon = [BeaconCount,"Estimote #3 Beacon", pixelConv(188), pixelConv(57),  "f8:04:2e:bf:c2:65", 740, 4735, -64, 188, 57]
BeaconList.append(Beacon)
BeaconCount += 1

Beacon = [BeaconCount,"Estimote #4 Beacon", pixelConv(198), pixelConv(135),  "5a:44:d7:bc:d0:36", 28495, 8272, -64, 198, 135]
BeaconList.append(Beacon)
BeaconCount += 1

Beacon = [BeaconCount,"Estimote #5 Beacon", pixelConv(272), pixelConv(145),  "71:c4:3d:c4:78:d6", 13072, 42423, -64, 272, 145]
BeaconList.append(Beacon)
BeaconCount += 1

Beacon = [BeaconCount, "ParticleFirst Beacon", pixelConv(315), pixelConv(435),  "dc:56:e7:49:39:f3", 0, 0, -73, 315, 435]
BeaconList.append(Beacon)
BeaconCount += 1

Beacon = [BeaconCount, "ParticleSecond Beacon", pixelConv(290), pixelConv(470), "32:dd:60:b6:bd:e9", 1, 1, -73, 290, 470]
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

LightList=[]
LightCount = 0
Light = [LightCount, "Lab Left", pixelConv(330), pixelConv(435),330, 435,0, 25] 
LightList.append(Light)
LightCount += 1

Light = [LightCount, "Lab Right", pixelConv(330), pixelConv(490), 330, 490, 0, 25] 
LightList.append(Light)
LightCount += 1

Light = [LightCount, "Living Room Top Left", pixelConv(147), pixelConv(36), 147, 36, 0, 39] 
LightList.append(Light)
LightCount += 1

Light = [LightCount, "Living Room Top Right", pixelConv(188), pixelConv(47), 188, 47, 0, 38] 
LightList.append(Light)
LightCount += 1

Light = [LightCount, "Living Room Lower Right", pixelConv(188), pixelConv(135), 188, 135, 0, 8] 
LightList.append(Light)
LightCount += 1


Light = [LightCount, "Living Room Left Bloom", pixelConv(137), pixelConv(126), 137, 126, 0, 40] 
LightList.append(Light)
LightCount += 1


Light = [LightCount, "Living Room Right Bloom", pixelConv(237), pixelConv(25), 237, 25, 0, 41] 
LightList.append(Light)
LightCount += 1


Light = [LightCount, "Right Bedroom", pixelConv(31), pixelConv(59), 31, 59, 0, 26] 
LightList.append(Light)
LightCount += 1


Light = [LightCount, "Left Bedroom", pixelConv(32), pixelConv(115), 31, 115, 0, 58] 
LightList.append(Light)
LightCount += 1


