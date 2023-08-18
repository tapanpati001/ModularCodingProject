import os,sys
from pathlib import Path
import logging 
while True:
    project_name=input("Enter Your Project Name: ")
    if project_name != "":
        break

#src/__init__.py (Let src is our project name)
#src/components/__init__.py (We want another file inside our project name)

list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    f"schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"
]
##spliting the files 
for filepth in list_of_files:
    filepath=Path(filepth)
    filedir,filename=os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True) #exist_ok if path is not present then it create the file path 

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass 
    else:
        logging.info("file is already present at :{filepath}")





