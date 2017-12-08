# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 08:43:36 2017

@author: njm58563
"""
# -*- coding: utf-8 -*-
"""
@author: njm58563
"""
import netCDF4 as nc
import csv
import numpy as np

def geo_idx(dd, dd_array):
   geo_idx = (np.abs(dd_array - dd)).argmin()
   return geo_idx


with open('C://Users//njm58563//Desktop//PIREPclean.csv') as csv_PIREPS:
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

out_file = open("C:/Users/njm58563/Desktop/PIREPtestturb.csv",'wb')
writer = csv.writer(out_file)
writer.writerow(data.keys()+['10m Northward Wind','10m Eastward Wind','50m Northward Wind','50m Eastward Wind'])   

for x in np.arange(0,len(datetime)):
        date=datetime[x]
        day = date[0:8]
        hr = date[8:10]
        mn = date[10:12]
        
        lati=float(latitude[x])
        loni=float(longitude[x])
    
        MERAfile =  nc.Dataset("C:/Users/njm58563/Desktop/MERA2/MERRA2_400.inst1_2d_asm_Nx."+day+".nc4",'r')
        lats = np.copy(MERAfile.variables['lat'][:])
        lons = np.copy(MERAfile.variables['lon'][:])
        mtimes = np.copy(MERAfile.variables['time'][:])

        targ_hr = int(hr)*60. + int(mn)
        
        time_idx = abs(mtimes - targ_hr).argmin()

        lat_idx = geo_idx(lati, lats)
        lon_idx = geo_idx(loni, lons)

    
        V10M = np.copy(MERAfile.variables['V10M'][time_idx,lat_idx,lon_idx])
        U10M = np.copy(MERAfile.variables['U10M'][time_idx,lat_idx,lon_idx])
        V50M = np.copy(MERAfile.variables['V50M'][time_idx,lat_idx,lon_idx])   
        U50M = np.copy(MERAfile.variables['U50M'][time_idx,lat_idx,lon_idx])   
 
        pdata = [data[t][x] for t in data.keys()]
        arrays = pdata + [V10M,U10M,V50M,U50M]   
        writer.writerow(arrays)
       
MERAfile.close()
    

    
