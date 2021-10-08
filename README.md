# TROPOMI SIF
All things related to TROPOMI SIF

## Original gridded files from Philipp

The original nc files from Philipp likely need to be permuted because the x,y,z order of the nc is out of order. Details are below. Check the code folder for the code I used to permute the NC files and extract the TIFFs. 

Also, I found that the extent was slightly off for the WGS84 rasters, for some reason. Using the SIF_extent.R code I fixed the extent and output to the 'fixed' folder. Use this data. 

### A more detailed explaination

https://gdal.org/drivers/raster/netcdf.html

The NetCDF driver assume that data follows the CF-1 convention from UNIDATA The dimensions inside the NetCDF file use the following rules: (Z,Y,X). If there are more than 3 dimensions, the driver will merge them into bands. For example, if you have an 4 dimension arrays of the type (P, T, Y, X). The driver will multiply the last 2 dimensions (P*T). The driver will display the bands in the following order. It will first increment T and then P. Metadata will be displayed on each band with its corresponding T and P values.

I was able to use NCO and the ncpdq command to permute the dimension fields so that the ncdf driver would read them correctly. For reference: http://nco.sourceforge.net/nco.html#ncpdq-netCDF-Permute-Dimensions-Quickly.

The command I used was: ncpdq -a time,lat,lon input.nc output.nc

Note that changing the dimensions when importing (in R) the nc file using the brick() function will likely not solve the problem (e.g. brick_sif_dc <- brick(file, varname = "sif_dc", dims = c(2, 3, 1))).

