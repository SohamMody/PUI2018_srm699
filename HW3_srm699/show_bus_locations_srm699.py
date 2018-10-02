from __future__ import print_function
import pandas as pd
import sys
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python  aSimplePythonScript.py <MTA-key> <Bus-line>")
    sys.exit()
url= "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+sys.argv[1]+"&VehicleMonitoringDetailLevel=calls&LineRef="+sys.argv[2]
mta=pd.read_json(url)
print("Bus Line: "+sys.argv[2])
active=len(mta['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
print("Number of active buses: %d"%active)
for i in range(0,active):
    print("Bus %d is at latitude %f and longitude %f"%(i,mta['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],mta['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))