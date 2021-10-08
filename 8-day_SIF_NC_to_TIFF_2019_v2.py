#-------------------------------------------------------------------------------
# Name:         Subdataset from NC to GeoTIFF
# Purpose:      Creates new raster from NetCDF subdataset. 
#
# Author:      Russell Doughty
#
# Created:     October 15, 2019
#
#-------------------------------------------------------------------------------


import os
from osgeo import gdal
#import gdal
#import rasterio
#import numpy as np
#from gdalconst import *
from tqdm import tqdm

# Define input variables
input_file = r'\\isilondata.rccc.ou.edu\eomfdata\TROPOMI\gridded\official-Philipp\permuted\MODIS-like_TROPOMI-SIF_2018-2020_perm.nc'
output_dir = r'\\isilondata.rccc.ou.edu\eomfdata\TROPOMI\gridded\official-Philipp\2019-new'
sub_data = ['sif_dc','cloud_fraction','n','phase_angle','sif_sigma'] #use gdalinfo code below to determine band needed
year = str(2019)
noDvalue = -9999

# The MODIS-like_TROPOMI-SIF_2018-2020.nc file contains 2018 data at the wrong time step. Only extract 2019 data.
startTime = 38 # 2019 starts at the 38th time step


def ncTIF(input_file,output_dir):
   
    print('Starting the run.')
    print('Input file is %s.' % input_file)
        
    #Use this to get the subdataset name
#    command = 'gdalinfo %s' % input_file
#    os.system(command)
#    command = 'gdalinfo %s' % 'NETCDF:"' + input_file+ '":' + sub_data[0]
#    os.system(command)
    
    # Create ouptut directory
    
    for i in range(len(sub_data)):
        direct = os.path.join(output_dir,sub_data[i])
        try: 
            os.makedirs(direct)
        except OSError:
            if not os.path.isdir(direct):
                raise 

    firstList_2019 = list(range(1,362,8))
    firstList_2019 = [str(item).zfill(3) for item in firstList_2019]
    lastList_2019 = list(range(8,361,8))
    lastList_2019.append(3)
    lastList_2019 = [str(item).zfill(3) for item in lastList_2019]
    
    for i in tqdm(range(len(sub_data))):
    
        fileSub = 'NETCDF:"' + input_file + '"' + ':' + sub_data[i] #combine inputfile name and subdataset name for gdal command - filename must be in double quotes
        
        for h in range(len(firstList_2019)):
                
            # Set output filename and directory
            output_file = 'TROPOMI.' + sub_data[i].upper() + '.' + year + '.' + firstList_2019[h] + '.' + lastList_2019[h] + '.tif'
            output_total = os.path.join(output_dir,sub_data[i], output_file)
                      
            #src_ds = gdal.Open('NETCDF:"' + ncList[h]+ '":' + sub_data) # for multiple NC files
            #src_ds = gdal.Open('NETCDF:"' + input_file+ '":' + sub_data[i]) # for single NC file (with multiple bands)
            
            #gdal.Translate(output_total, src_ds, format = 'GTiff', bandList = [h+1]) # Use band list if the nc file has a series of bands, like time
            
            # Output to tiff with gdal
            command = 'gdal_translate -of GTiff -b %s %s %s' % (h+startTime,fileSub,output_total)
            os.system(command)
            
            print('')
            print('Created %s.' % output_file)
            print('Time step is %s.' % str(h+startTime))
            print('')
            
        print('Done with DOY %s.' % firstList_2019[h])
        print('')
                                    
    print ('Run FINISHED.')

    
ncTIF(input_file,output_dir)