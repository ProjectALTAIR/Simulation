"""
The Transition Model.
Init: State object with information about current location & ground velocity, the action
which will be taken, and an environment object containing wind information 
and simulation parameters.

This is done as an object so that multiple models may be used at the same time for 
reinforcement learning techniques. For example, learning the true environment given
an approximation. The AI could learn from a predicted weather environment, but the 
tm could uses the real data.
"""

class Tm:
    def __init__(self,state,action,environment):

"""
update() computes the n+1 state and updates state location/velocity assigning nth state
to the associated object variables for previous states, and the new n+1 to be the current
state.
"""
    def update(self,state,action,environment):
        return state