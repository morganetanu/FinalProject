# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 10:40:59 2017

@author: njm58563
"""

# -*- coding: utf-8 -*-
"""
@author: njm58563
"""
import netCDF4 as nc
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap

def geo_idx(dd, dd_array):
   geo_idx = (np.abs(dd_array - dd)).argmin()
   return geo_idx

# extract the variables you want
# set variables to constants to test script        
datetime = '201701042244'
latitude = 42.19401
longitude = -72.92578021






date=datetime
lati=float(latitude)
loni=float(longitude)
day = date[0:8]
hr = date[8:10]
mn = date[10:12]

MERAfile =  nc.Dataset("C:/Users/njm58563/Desktop/MERRA2_400.inst1_2d_asm_Nx."+day+".nc4",'r')
lats = np.copy(MERAfile.variables['lat'][:])
lons = np.copy(MERAfile.variables['lon'][:])
mtimes = np.copy(MERAfile.variables['time'][:])
targ_hr = int(hr)*60. + int(mn)
time_idx = abs(mtimes - targ_hr).argmin()\

V10M = np.copy(MERAfile.variables['V10M'][time_idx,:,:])
U10M = np.copy(MERAfile.variables['U10M'][time_idx,:,:])
V50M = np.copy(MERAfile.variables['V50M'][time_idx,:,:])   
U50M = np.copy(MERAfile.variables['U50M'][time_idx,:,:]) 
MERAfile.close()  
 
mag10M = (U10M**2+V10M**2)**0.5
    
map = Basemap(projection='merc',llcrnrlon=-80.,llcrnrlat=35.,urcrnrlon=-65.,urcrnrlat=45.,resolution='i')
map.drawcoastlines()
map.drawstates()
map.drawcountries()
#map.drawlsmask(land_color='Linen', ocean_color='#CCFFFF')
parallels = np.arange(0,65,5.) # make latitude lines ever 5 degrees from 30N-50N
meridians = np.arange(-135,-45,5.) # make longitude lines every 5 degrees from 95W to 70W
map.drawparallels(parallels,labels=[1,0,0,0],fontsize=5)
map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=5) 
x,y = np.meshgrid(lons,lats)
xp,yp= map(longitude, latitude) 
map.plot(xp, yp, 'bo', markersize=7)
            
xi,yi = map(x,y)
wind = map.pcolormesh(xi,yi,mag10M, cmap='Reds')
clevs = np.arange(960,1040,4)
map.barbs(xi[::4,::4],yi[::4,::4],U10M[::4,::4],V10M[::4,::4])
#cs = map.contour(x,y,V10M[0,:,:]/100.,clevs,colors='blue',linewidths=1.)
#plt.clabel(cs, fontsize=9, inline=1) # contour labels
plt.title('10m Wind'+datetime)    
plt.show()


mag50M = (U50M**2+V50M**2)**0.5
    
map = Basemap(projection='merc',llcrnrlon=-80.,llcrnrlat=35.,urcrnrlon=-65.,urcrnrlat=45.,resolution='i')
map.drawcoastlines()
map.drawstates()
map.drawcountries()
#map.drawlsmask(land_color='Linen', ocean_color='#CCFFFF')
parallels = np.arange(0,65,5.) # make latitude lines ever 5 degrees from 30N-50N
meridians = np.arange(-135,-45,5.) # make longitude lines every 5 degrees from 95W to 70W
map.drawparallels(parallels,labels=[1,0,0,0],fontsize=5)
map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=5) 
x,y = np.meshgrid(lons,lats)
xp,yp= map(longitude, latitude) 
map.plot(xp, yp, 'bo', markersize=7)
            
xi,yi = map(x,y)
wind = map.pcolormesh(xi,yi,mag10M, cmap='Reds')
clevs = np.arange(960,1040,4)
map.barbs(xi[::4,::4],yi[::4,::4],U50M[::4,::4],V50M[::4,::4])
#cs = map.contour(x,y,V10M[0,:,:]/100.,clevs,colors='blue',linewidths=1.)
#plt.clabel(cs, fontsize=9, inline=1) # contour labels
plt.title('50m Wind'+ datetime)    
plt.show()    