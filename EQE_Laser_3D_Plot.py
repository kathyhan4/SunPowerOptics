# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 15:08:29 2015

@author: khan
"""

import csv
import os
from numpy import array
import numpy
import datetime
#from datetime import datetime
import time
import matplotlib.pyplot as plt
import dateutil
from pylab import *
import bisect
from mpl_toolkits.mplot3d.axes3d import Axes3D

rootdir= 'C:\\Users\\khan\\Documents\\GitHub\\SunPowerOptics\\'

filenamelocation = rootdir+'LBIC SPWR Cu, 640nm, 60micron FWHM 30micW beam.csv'

DataFile = open(filenamelocation)
data = numpy.recfromcsv(DataFile, delimiter=',', filling_values=numpy.nan, case_sensitive=True, deletechars='', replace_space=' ')
    
size2=len(data[0])
print size2
size3=size(data)
print size3

numarray = numpy.zeros((len(data),size2)) 

for i in range(len(data)):
   x = data[i]
   for j in range(len(x)):
      numarray[i,j] = x[j]

size4 = numarray.shape      
print size4

#xdim = zeros(size3)
#ydim = zeros(size2)

xdim = range(0,size3)
ydim = range(0,size2)

fig = plt.figure(figsize=(14,6))

# `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot
#ax = fig.add_subplot(1, 2, 1, projection='3d')
#
#p = ax.plot_surface(xdim, ydim, numarray, rstride=4, cstride=4, linewidth=0)

# surface_plot with color grading and color bar
ax = fig.add_subplot(1, 1, 1, projection='3d')
p = ax.plot_surface(xdim, ydim, numarray, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)
      
#print numarray.shape
#
#for i in range(len(timearray)):
#   numarray[i,20] = timearray[i]
#   numarray[i,33] = (numarray[i,20]-numarray[0,20])/3600
#
#shapenumarray = numarray.shape
#
#hvlist_length = []
#lvlist_length = []
#
#for i in range(0,len(timearray)):
#    x = numarray[i]
#    if numarray[i,MeasVoltColumn] < VoltageBias/2:
#        hvlist_length.append(x)
#
#    elif numarray[i,MeasCurColumn] > Current4Wire/2:
##    elif numarray[i,MeasVoltColumn] > 0 and numarray[i,MeasCurColumn] > Current4Wire/2:
#        lvlist_length.append(x)
#
#hvlist = numpy.zeros((len(hvlist_length),numbercolumns))
#lvlist = numpy.zeros((len(lvlist_length),numbercolumns))
#
#k=0
#l=0
#
#
#for i in range(0,len(timearray)):
#   if numarray[i,MeasVoltColumn] < VoltageBias/2:
#       for j in range(0,numbercolumns):
#          hvlist[k,j] =numarray[i,j]
#       k=k+1
#   elif numarray[i,MeasCurColumn] > Current4Wire/2:
#       for m in range(0,numbercolumns):
#          lvlist[l,m] = numarray[i,m]
#       l=l+1
#with open('LBIC SPWR Cu, 640nm, 60micron FWHM 30micW beam.csv', 'rb') as csvfile:
#     EQEresults = csv.reader(csvfile, delimiter=',', quotechar='|')
#     for row in spamreader:
#         print ', '.join(row)