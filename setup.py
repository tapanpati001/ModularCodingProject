from setuptools import setup,find_packages
from typing import List 

PROJECT_NAME="Machine Learning Project"
VERSION="0.0.1"
DESCRIPTION="This is a machine learning project in modular coding"
AUTHOR_NAME="Tapan Kumar Pati"
AUTHOR_EMAIL="tpati2001@gmail.com"




REQUIREMENTS_FILE_NAME="requirements.txt"

HYPEN_E_DOT="-e ."

# Requirements.txt file open
# read
# \n replace to "" 
def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_files:
        requirement_list = requirement_files.readlines()
        requirement_list= [requirement_name.replace("\n","") for requirement_name in requirement_list]

        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)

        return requirement_list

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires= get_requirements_list()
      
    )