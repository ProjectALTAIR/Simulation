import pandas as pd

def generate_env(u_file,v_file):
	u_env=pd.read_csv(u_file,names=['a','b','c','alt','lon','lat','u_val'])
	v_env=pd.read_csv(v_file,names=['a','b','c','alt','lon','lat','v_val'])
	#adds the v_val column to u_val.
	env=pd.concat([u_env[['alt','lon','lat','u_val']],v_env['v_val']], axis=1, join_axes=[u_env.index])
	return env

def save_env(out_filename,env):
	env.to_csv(out_filename)
	print "Saved to: " + out_filename

def load_env(in_filename):
	env=pd.read_csv(in_filename)
	env=env[['alt','lon','lat','u_val','v_val']]
	print "Loaded: " + in_filename
	return env