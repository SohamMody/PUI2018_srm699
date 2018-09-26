from __future__ import print_function
import pandas as pd
import sys
if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python  aSimplePythonScript.py <MTA-key> <Bus-line> <BUS_LINE>.csv")
    sys.exit()
url= "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+sys.argv[1]+"&VehicleMonitoringDetailLevel=calls&LineRef="+sys.argv[2]
mta=pd.read_json(url)
active=len(mta['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
fout = open(sys.argv[3], "w")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")
for i in range(0,active):
    thisline = "" 
    for j in range(0,len(mta['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'])):
        thisline += "%f,%f,"%(mta['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],mta['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
        if(mta['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']!=""):
            sn=mta['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][j]['StopPointName']
        else:
            sn="N/A"
        if(mta['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']!=""):
            pd=mta['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][j]['Extensions']['Distances']['PresentableDistance']
        else:
            pd="N/A"
        thisline += "%s,%s"%(sn,pd)
        #.strip(',') removes the last comma
        fout.write(thisline+"\n")