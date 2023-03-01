import json, os
from main import login

def clear():
	cls = lambda: os.system("clear")
	cls()
	print(""" __                           
/   __ _  _| o _|_|V| _ _|_ _ 
\__ | (/_(_| |  |_| |(_| |_(/_""" + "\n")

def reset(msg):
	clear()
	print(msg)
	login()

def print_dict(dict):
	for item, value in dict.items():
		print("{}: {}".format(item, value))
	print()

def update_json(file, data, new_data):
	data.update(new_data)
	with open(file, "w") as f:
	  json.dump(data, f, indent=2)