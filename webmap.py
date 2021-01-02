# webmap.py
# builds the webmap code from state and configuration files
# jcs 6/9/2014
#
from builtins import str
import utils
# if conflocal.py is not found, import default conf.py


# Check for user imports
try:
        import conflocal as conf
except ImportError:
        import conf


def buildWebMapToFile(myPosition, rollingRSSIArray, currentLightStateArray, displaybeacon, displaylights):

        #print currentLightStateArray
		
        f = open("/home/pi/SDL_Pi_BeaconAir/state/beacon.html", "w")
        fh = open("/home/pi/SDL_Pi_BeaconAir/state/beaconheader.txt", "r")
        ff = open("/home/pi/SDL_Pi_BeaconAir/state/beaconfooter.txt", "r")

        webresponse = ""	

        if (displaybeacon == True):	
            for beacon in conf.BeaconList:

                webresponse += "<img src='" 
                webresponse += "iBeacon.png' style='position: absolute; top: "
                webresponse +=  str(beacon[9]-17)
                webresponse +=	"px; left: " + str(beacon[8]-15) +"px;'/>\n"
	
                #webresponse += "<BR class='transparent-circle' style='height:"
                #webresponse += str(conf.meterToPixel(utils.calculateDistanceWithRSSI(rollingRSSIArray[beacon[0]], beacon[0])) )
                #webresponse += "; width:"
                #webresponse += str(conf.meterToPixel(utils.calculateDistanceWithRSSI(rollingRSSIArray[beacon[0]], beacon[0])) )
                #webresponse += "; position: absolute; top:"
                #webresponse += str(beacon[9]- conf.meterToPixel(utils.calculateDistanceWithRSSI(rollingRSSIArray[beacon[0]], beacon[0])))
                #webresponse += "; left: "
                #webresponse += str(beacon[8]- conf.meterToPixel(utils.calculateDistanceWithRSSI(rollingRSSIArray[beacon[0]], beacon[0])))
                #webresponse += "; >\n"
	
        if (displaylights == True):	
            for light in conf.LightList:
                	
                webresponse += "<img src='" 
                if (currentLightStateArray[light[0]] == True):
                    webresponse += "OnLightBulb.png' style='position: absolute; top: "
                else:
                    webresponse += "OffLightBulb.png' style='position: absolute; top: "
                webresponse +=  str(light[5]-17)
                webresponse +=	"px; left: " + str(light[4]-15) +"px;'/>\n"
	
        # now do my Position
        # minus means old position
        if ((myPosition[0] > 0.0) and (myPosition[1] > 0.0)):
            webresponse += "<img src='"
            webresponse += "red-pin.png' style='position: absolute; top: "
            webresponse +=  str(conf.meterToPixel(myPosition[1])-17)
            webresponse +=	"px; left: " + str(conf.meterToPixel(myPosition[0])-15) +"px;'/>\n"
        else:	
            myPosition = [-myPosition[0], -myPosition[1]]
            webresponse += "<img src='"
            webresponse += "blue-pin.png' style='position: absolute; top: "
            webresponse +=  str(conf.meterToPixel(myPosition[1])-17)
            webresponse +=	"px; left: " + str(conf.meterToPixel(myPosition[0])-15) +"px;'/>\n"
		

        webheader = fh.read()
        webfooter = ff.read()

        #print webresponse
        f.write(webheader)
        f.write(webresponse)
        f.write(webfooter)

        f.close()
        fh.close()
        ff.close()

