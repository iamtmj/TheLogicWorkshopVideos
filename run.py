import os
nameClass=input("Name of the class:")
currentDir=os.getcwd()
dirCommand=f"cd {currentDir}"
execCommand=f"py -m manim main.py {nameClass} -p"
os.system(dirCommand)
os.system(execCommand)