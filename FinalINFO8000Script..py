# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 14:04:38 2017

@author: njm58563
"""
import netCDF4 as nc
import csv
import numpy as np

def geo_idx(dd, dd_array):
   geo_idx = (np.abs(dd_array - dd)).argmin()
   return geo_idx


with open('C:/Users/njm58563/Desktop/SamplePIREPs.csv') as csv_PIREPS:
  reader = csv.DictReader(csv_PIREPS)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

# extract the variables you want
# set variables to constants to test script        
#datetime = '20170101'
#latitude = 42.80321293
#longitude = -94.79914694
datetime = data['VALID']
latitude = data['LAT']
longitude = data ['LON']

for x in np.arange(0,len(datetime)):
    date=datetime[x]
    lati=float(latitude[x])
    loni=float(longitude[x])
    
    
    
    MERAfile =  nc.Dataset("E:/MERA2/MERRA2_400.inst1_2d_asm_Nx."+date+".nc4",'r')
    lats = np.copy(MERAfile.variables['lat'][:])
    lons = np.copy(MERAfile.variables['lon'][:])
 

    lat_idx = geo_idx(lati, lats)
    lon_idx = geo_idx(loni, lons)

    
    V10M = np.copy(MERAfile.variables['V10M'][:,lat_idx,lon_idx])
    U10M = np.copy(MERAfile.variables['U10M'][:,lat_idx,lon_idx])
    V50M = np.copy(MERAfile.variables['V50M'][:,lat_idx,lon_idx])   
    U50M = np.copy(MERAfile.variables['U50M'][:,lat_idx,lon_idx])   
    SLP = np.copy(MERAfile.variables['SLP'][:,lat_idx,lon_idx])
    TROPPB = np.copy(MERAfile.variables['TROPPB'][:,lat_idx,lon_idx])
    
    names = ['10m Northward Wind','10m Eastward Wind','50m Northward Wind','50m Eastward Wind','Sea-Level Pressure','Tropopause Pressure']    

    arrays = [names,V10M,U10M,V50M,U50M,SLP,TROPPB]    
    with open("C://Users//njm58563//Desktop//PIREPtest"+date+".csv",'w') as f:
        writer = csv.writer(f)
        writer.writerows(arrays)
 
    MERAfile.close()