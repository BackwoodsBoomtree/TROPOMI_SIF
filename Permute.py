

## SOURCE ###
############# http://nco.sourceforge.net/nco.html#ncpdq-netCDF-Permute-Dimensions-Quickly #######

## Before extracting GeoTIFFs from the TROPOMI NC file, we must permute the time dimension.
# Copy and paste this code into the terminal:

ncpdq -a time,lat,lon input.nc output.nc

# For this to work, you must install nco using conda:

conda install -c conda-forge nco

# It might be necessary to create and activate a new environment before installing:
conda create --name nco
actiavte nco

# NOTE: Both the code and data must be either on the server or both on desktop.