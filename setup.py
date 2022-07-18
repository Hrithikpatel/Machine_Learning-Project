from setuptools import setup 
from typing import List


#Declaring variables for setup

project_name="housing prediction"
author="Hrithik Patel"
version="0.0.1"
package=["housing"]
license="Apache"
requirement_file='requirements.txt'

def get_requirement()->List[str]:

    """"
    This function is going to return a list of libraries mention 
    in requirements.txt file
    """
    with open(requirement_file,'r') as requirements:
         return requirements.readlines()


setup(
    project_name=project_name,
    author=author,
    version=version,
    packages=package,
    license=license,
    install_requires=get_requirement()



)