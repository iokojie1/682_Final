# District of Columbia (DC) Shot Spotter Gunshot Analysis, Wednesday July 31, 2019, Irenosen Okojie

Introduction

This analysis is to assist the Washington DC Metropolitan Police Department (MPD) in expanding there Shot Spotter gunshot detection network. Since this network currently operates only in the areas that historically had higher crimes, I used QGIS and python to determine the areas that currently have high crimes rates and that the gunshot detection network needs to cover in the future. 

Analysis

Shooting Incidents is a point dataset for Shot Spotter gunshot detection that uses sensors to detect, locate and alert law enforcement agencies of potential gunfire incidents in real time. Link: https://opendata.dc.gov/datasets/89bfd2aed9a142249225a638448a5276_29
District of Columbia Wards is a dataset that contains the polygons that represent the boundaries of DC from the 2012 election. Link: https://opendata.dc.gov/datasets/ward-from-2012
Gun Crimes is the point dataset selected from all the gun methods from the Crimes Incidents in 2017 dataset, which contains a subset of locations and attributes of incidents reported in the Analytical Services Application crime report database by the MPD. Link: https://opendata.dc.gov/datasets/crime-incidents-in-2017
In order to create my maps I used the field calculator to create two formulas: the number of gun crimes or shooting incidents per person, then multiply by 10,000 to a new field named POPDEN. Then used the style tab to graduate my POPDEN layer by their classification using an equal interval mode. Then in map editor mode completed my map with the appropriate map symbols(Title, legend, north arrow, etc.).  
