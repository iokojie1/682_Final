#Irenosen Okojie
#Tuesday, July 30th, 2019
#GEOG 682 Final

import processing #import QGIS processing tools

#Loads three datasets
guncrimes = "/Users/Ren/Final Project/Gun_Crimes.gpkg"
shot_spotter_gun_shots =  "/Users/Ren/Final Project/Shot_Spotter_Gun_Shots/Shot_Spotter_Gun_Shots.shp"
wards = "/Users/Ren/Final Project/Ward_from_2012/Ward_from_2012.shp"

#Display datasets to map
a = iface.addVectorLayer(guncrimes, "Gun Crimes in 2017", "ogr")
b = iface.addVectorLayer(shot_spotter_gun_shots, "Shooting Incidents", "ogr")
c = iface.addVectorLayer(wards, "Wards", "ogr")

a_feature=a.featureCount() #count amount of gun crimes 
b_feature=b.featureCount() #count amount of shooting incidents
print("number of gun crimes: ", a_feature) #Display number of gun crimes
print("number of shooting incidents", b_feature) #Display number of shooting incidents

c_feature=c.getFeatures() #request feature

for f in c_feature:
    d = f.attributes()[2] #NAME attributes
    e = f.attributes()[14] #POP_2010 attributes
    print ("DC Population in 2010 of",d, "is", e, "people") #Display DC population by Ward
    g = (a_feature/e)*10000 # calculate the number of gun crimes committed per 10,000 people in 2017 in each ward
    print("Gun crimes committed per 10,000 people in 2017 in", d, "is", g) #print the results
    h = (b_feature/e)*10000 #calculate the number of shooting incidents detected by ShotSpotter per 10,000 people in 2017 in each ward
    print("Shooting incidents detected by ShotSpotter per 10,000 people in 2017 in", d, "is", h) #print the results