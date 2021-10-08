#-------------------------------------------------------------------------------
# Name:        Aggregate 
# Purpose:    
#
#               
#
# Author:      Russell Doughty
#
# Created:     October 6 2019
#-------------------------------------------------------------------------------

import os

input_dir = r'\\isilondata.rccc.ou.edu\eomfdata\TROPOMI\gridded\official-Philipp\2019-new'
output_dir = r'\\isilondata.rccc.ou.edu\eomfdata\TROPOMI\gridded\official-Philipp\4326\2019-new'

test = os.walk(input_dir)

# Recreate subdirectories
for dirpath, dirnames, filenames in os.walk(input_dir):
    structure = os.path.join(output_dir, os.path.relpath(dirpath, input_dir))
    if not os.path.isdir(structure):
        os.mkdir(structure)
    else:
        print("Folder already exits!")
        
for dirpath, dirnames, filenames in os.walk(input_dir):
    inpath = os.path.join(input_dir, os.path.relpath(dirpath, input_dir))
    outpath = os.path.join(output_dir, os.path.relpath(dirpath, input_dir))
       
    if len(filenames) > 0:
        
        for i in range(len(filenames)):
            infile = os.path.join(inpath,filenames[i])
            outfile = os.path.join(outpath,filenames[i])
        
            command = 'gdalwarp -t_srs EPSG:4326 -dstnodata -9999 -overwrite %s %s' % (infile,outfile)
            os.system(command)
    
print('DONE!!')