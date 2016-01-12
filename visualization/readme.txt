Dynamic plotting of flightpaths in Google Earth.

Usage:
========================================
1) Install Google Earth

https://www.google.com/earth/
========================================
2) Run generate_path(path,setup)
'path' must be an array containing strings of the form "Longitude,Latitude,altitude(meters)"
'setup' will contain the path plotting parameters such as colour, opacity, and line-width.
========================================
3) Load flightpath.kml and then refresh.kml in Google Earth.
========================================
4) Done. Any changes to flightpath.kml will be dynamically updated in Google Earth.
========================================

To do:
- Figure out colouring/opacity/line-width options so that a setup file can be utilized. This would
allow a sort of density cloud of the long term flight path for better visualization.