from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> list:
    """function to get the list of requirements from a file
    """
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()
            if line and not line.startswith("#"):
                requirements.append(line)
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)     
    return requirements


setup(
    name="ml_project",
    version="0.0.1",
    author="nandhakumar",
    author_email="nandhakumargs8877@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
    )