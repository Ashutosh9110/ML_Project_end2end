from setuptools import setup
from typing import List


# Declaring variables for set up functions
Project_name="housing-predictor"
version="0.0.1"
author="Ashutosh Singh"
description=" This project that aims to generate housing appraisals to determine values of properties"
packages=["housing"]
requirements_file_name="requirements.txt"

def get_requirements_list()->List[str]: # It sapys that this function will return a list which will have string in it.
    """
    Description: This function is going to return a list of requirements mentioned in the requirements.txt file.

    return This functin will return a list which will contain name of libraries mentioned in the requirements.txt file
    """
    with open(requirements_file_name) as requirement_file:
        return requirement_file.readlines()

setup(
name=Project_name,
version=version,
author=author,
description=description,
packages=packages,
install_requires=get_requirements_list()

)

# if __name__ == "__main__":
#     print(get_requirements_list())