Generating the environmental data.

Usage:
========================================
1) Install wgrib2. Details here:

http://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/compile_questions.html

Requires: gcc and gfortran.
========================================
2) Select a region (longitude/latitude in degrees) and individually extract the u and v components into a csv file. This is done with:

wgrib2 -match ":(<component name>):(<pressures>)"  <gfs filename> -undefine out-box <lon_min>:<lon_max> <lat_min>:<lat_max> -csv <path/name of out csv file>
----------

"-match" is a regex to select the relevant data. To select multiple things separate with a "|" like so "10 mb|20 mb"

For this project we only need to worry about are:
	(UGRD, VGRD) - The u and v components of the winds ground velocity.
	(10 mb, 20 mb, 30mb, 50 mb, 70 mb, 100 mb) - The relevant pressure regions.
----------

"-undefine out-box" simply sets all data outside of the specified lat/lon region to be undefined. This allows us to easily save only only the selected region.
----------

example:
wgrib2 -match ":(VGRD):(10 mb|20 mb|30 mb|50 mb|70 mb|100 mb)"  gfs.f003 -undefine out-box -157:-154 18:21 -csv /media/james/New\ Volume/v.csv

This example selects the v component at the relevent pressures from the file "gfs.f003" in the region "-157:-154 18:21" (the region approximately over Mauna Kea). It then saves it to my second hard-drive as "v.csv".
========================================
3) Prepare the environment by loading it into pandas dataframes. The output of csv files which wgrib2 gives contain a lot of junk. This is removed by using generate_env(u_file,v_file) which will return a clean and easily usable version of the data. Note step 2) must be done twice to generate the two files for both the u and v components. generate_env(u_file,v_file) will combine these two files as well as clean up the data.

The data may then be saved and reloaded for later use by using save_env(out_filename,env) and load_env(in_filename) respectively.

Requires: pandas
========================================
4)The environment data is ready to run. If secondary learning agent is being employed then two sets of environmental data must be created. One will have the predicted wind data, and the second will have the "observed" wind data.