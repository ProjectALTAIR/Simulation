"""
Project ALTAIR sky coverage simulation
Author: James Hartwick
Version 1.8 - August 16, 2015
Aim: Suite of callable functions for simulation of high altitude balloon 
movement. Intended for use via scripts or via ipython with pylab.
"""
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def get_env(filename):
	#removed, instead read csc with pandas in ipython
	#ex:  env=pd.read_csv(filename)
def getReward(state,minAltitude,scale):
	#Simple version - calculates the reward based on a normal viewing angle (1,0,0)
	if (state[0][2]) < minAltitude:
		return -1.
	else
		return 1./np.sqrt(np.sum(np.square(state[0][0:2]/scale)))

def plot_density():
	#removed, instead plot with pandas in ipython
	#ex:  df.plot(kind='hexbin', x='a', y='b', gridsize=25)


def plot_hist():
	#$path.plot(kind='hexbin',x=0,y=1,gridsize=20)
	#path['angle']=np.arctan(np.sqrt((path['x']-50.)**2+(path['y']-50.)**2)/50.1)*3600
	#path['angle'].plot(kind='hist',bins=50,alpha=0.5)
	plt.title('Frequency of Path Location at a Given Annulus')
	plt.ylabel('Bin Frequency')
	plt.xlabel('Arcseconds')
	print path['angle'].mean()
	print path['angle'].var()

#################################################################################
# update_env(env)
# Updates and returns a new environment (R3 numpy array)
# Will make use of a Kalman Filter
#################################################################################
def update_env(env):
	return env
#################################################################################
# density_plot_a(path)
# Input path (3 column data frame containing)
#################################################################################
def density_plot(path,style='a'):
	if (style=='a'):
		print style
	elif ((style=='xy') or (style=='yx')):
		print style
	elif ((style=='xz') or (style=='zx')):
		print style
	elif ((style=='yz') or (style=='yz')):
		print style
#################################################################################
# get_stats(path)
#################################################################################
def get_stats(path):
	return path
#################################################################################
# load_env()
#################################################################################
def load_env(env_loc):
	print 1
	return env

#################################################################################
# Initial conditions
#################################################################################
""" Ignore - used for initital testing
v_max = .028
drag_coeff = 0.5
propulsive_efficiency = 0.8
update_time = 300
environment = (np.random.rand(100,100,100))*.2
centre = [50,50,50]
pos=[50.1,50.1,50.1]
w_dir=np.random.uniform(-1.,1,size=3)
w_norm=np.sqrt(w_dir[0]**2+w_dir[1]**2+w_dir[2]**2)
path = pd.DataFrame(pos).transpose()

#################################################################################
for i in range(0,1000):
	w_dir=np.random.uniform(-1.,1,size=3)
	w_norm=np.sqrt(w_dir[0]**2+w_dir[1]**2+w_dir[2]**2)

	pos = pos + (w_dir/w_norm)*environment[int(pos[0])][int(pos[1])][int(pos[2])] + v_max*(list(map(lambda x:x+np.random.uniform(-1.,1),centre))-pos/(np.sqrt((centre[0]-pos[0])**2+(centre[1]-pos[1])**2+(centre[2]-pos[2])**2)))

	if (i>=10): path=path.append(pd.DataFrame(pos).transpose())
path=path+0.6
path.columns=['x','y','z']
path['angle']=np.arctan(np.sqrt((path['x']-50.)**2+(path['y']-50.)**2)/50.1)*3600

"""