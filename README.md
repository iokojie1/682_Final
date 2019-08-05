# District of Columbia (DC) Shot Spotter Gunshot Analysis, Wednesday July 31, 2019, Irenosen Okojie

Introduction

This analysis is to assist the Washington DC Metropolitan Police Department (MPD) in expanding there Shot Spotter gunshot detection network. Since this network currently operates only in the areas that historically had higher crimes, I used QGIS and python to determine the areas that currently have high crimes rates and that the gunshot detection network needs to cover in the future. 

Analysis

Shooting Incidents is a point dataset for Shot Spotter gunshot detection that uses sensors to detect, locate and alert law enforcement agencies of potential gunfire incidents in real time. Link: https://opendata.dc.gov/datasets/89bfd2aed9a142249225a638448a5276_29
District of Columbia Wards is a dataset that contains the polygons that represent the boundaries of DC from the 2012 election. Link: https://opendata.dc.gov/datasets/ward-from-2012
Gun Crimes is the point dataset selected from all the gun methods from the Crimes Incidents in 2017 dataset, which contains a subset of locations and attributes of incidents reported in the Analytical Services Application crime report database by the MPD. Link: https://opendata.dc.gov/datasets/crime-incidents-in-2017
In order to create my maps I used the field calculator to create two formulas: the number of gun crimes or shooting incidents per person, then multiply by 10,000 to a new field named POPDEN. Then used the style tab to graduate my POPDEN layer by their classification using an equal interval mode. Then in map editor mode completed my map with the appropriate map symbols(Title, legend, north arrow, etc.).  
The number of gun crimes committed per 10,000 peoplein 2017 in each ward map:
https://raw.githubusercontent.com/iokojie1/682_Final/master/Gun%20Crimes%20per%20pop.jpg
The number of shooting incidents detected by ShotSpotter per 10,000 people in 2017 in each ward map:
https://raw.githubusercontent.com/iokojie1/682_Final/master/Shot%20Spotter%20Gun%20Shot%20per%20POP.jpg

List showing the number of gun crimes committed per 10,000 people in 2017 in each ward:

Ward 1	212.9
Ward 2	206.8
Ward 3	200.9
Ward 4	209.2
Ward 5	213.3
Ward 6	207.9
Ward 7	220.9
Ward 8	215.2

List showing the number of shooting incidents detected by ShotSpotter per 10,000 people in 2017 in each ward: 

Ward 1	4599.4
Ward 2	4468.4
Ward 3	4341.4
Ward 4	4519.8
Ward 5	4608.9
Ward 6	4492.2
Ward 7	4773.4
Ward 8	4649.3

Automation

My code is really simple and uses one for loop to calcaute both parts of my analysis. First used the get.features() method to call the features in my Wards layer. 

"c = iface.addVectorLayer(wards, "Wards", "ogr")

c_feature=c.getFeatures() #request feature "

Next created the for loop method to create a simple forumla for the analysis, earlier used the featureCount() method to count the amount of gun crimes and/or shooting incidences. Then used the print() method to print my results. 

"a_feature=a.featureCount() #count amount of gun crimes 

g = (a_feature/e)*10000 # calculate the number of gun crimes committed per 10,000 people in 2017 in each ward

print("Gun crimes committed per 10,000 people in 2017 in", d, "is", g) #print the results"

At first attempt for this analysis I tired using the processing.run("qgis:fieldcalculator") method since that the map was created in QGIS but the code had some errors and the results were only running the formula on the population for the 8th ward instead of all of them individually. 

Results

The wards that I recommend to becovered by an expanded gunshot detection network are Ward 1, 4, 5, 6, 7, 8.
My biggest limitation in my analysis is the population data; since it is only from 2010, the analysis maybe skewed since it was recorded almost a decade ago. Another limitation is just human error, when I first started I thought the gun crimes total was around 33,000 when in actually the total is 1584. Which is drastically different then what was first recorded, so I am hoping there are no more errors like that in my analysis. 

