# setuptools is a Python library used to create, distribute, and install Python packages.
# setup() is the main function used to define metadata for your project package like: Package name, dependencies, author name etc.
# find_packages: This function automatically finds all Python packages in project directory.
# typing module is used for type hinting.
# List indicates that a variable will store a list of items.

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str] = []
    try:
        with open("requirements.txt", 'r') as file:
            # Read lines from the files.
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst

# Setup Metadata
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Ritesh Kumar",
    author_email="riteshkumar8888@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)
