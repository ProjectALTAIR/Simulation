import pandas as pd

def setup():
	environment = Environment(pd.read_csv('setup.txt'))
	return environment