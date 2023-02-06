from setuptools import setup, find_packages
from typing import List


# Declaring variables for set up functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Ashutosh Singh"
DESCRIPTION="This project that aims to generate housing appraisals to determine values of properties"
# PACKAGES =["housing"]
# # Now instead of using this, we can use find_packages. It is a pre-built package that returns all the folder name.
# Whereever it will find __init__, it will use those folders as a packages.
requirements_file_name="requirements.txt"

def get_requirements_list()->List[str]:
    # It sapys that this function will return a list which will have string in it.
    """
    Description: This function is going to return a list of requirements mentioned in the requirements.txt file.

    return This functin will return a list which will contain name of libraries mentioned in the requirements.txt file
    """
    with open(requirements_file_name) as requirement_file:
        return requirement_file.readlines()
        # -e . will install all the required libraries that are in the housing folder.

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
# packages=find_packages(),
packages = find_packages(),
# packages=["housing"] # Now instead of using this, we can use find_packages. It is a pre-built package that returns all the folder name. 
# Whereever it will find __init__, it will use those folders as a packages.
install_requires = get_requirements_list()
)
# This states all the external libraries that are required for the program to run through.

# if __name__ == "__main__":
#     print(get_requirements_list())