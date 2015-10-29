"""
This class contains all information of the current state of the simulation including
both the original and post-update location and velocity information.

All location & velocity vectors are 3 component numpy arrays of the form 
[latitude,longitude,altitude] in meters. The zero point will be defined by
the given environment object.
"""

class State:
    def __init__(self,location,velocity):




