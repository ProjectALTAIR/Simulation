import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plot_actions():

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(vectors['x'],vectors['y'],vectors['z'])
	plt.show()

#Generates n equidistributed points on a unit sphere to build the ideal action space.
#This is a 3d generalization of vogels method of equidistant points on a disk.
def generate_actions(n):
	golden_angle = np.pi * (3 - np.sqrt(5))
	theta = golden_angle * np.arange(n)
	z = np.linspace(1 - 1.0 / n, 1.0 / n - 1, n)
	radius = np.sqrt(1 - z * z)
	points = np.zeros((n, 3))
	points[:,0] = radius * np.cos(theta)
	points[:,1] = radius * np.sin(theta)
	points[:,2] = z
	vectors = pd.DataFrame(points)
	vectors.columns = ['x','y','z']
	return vectors

