from setuptools import setup, find_packages
import os

VERSION = '0.0.1'
DESCRIPTION = 'CrowXeoHello Python'

# Setting up
setup(
    name="crowxeohello",
    version=VERSION,
    author="CrowXeo",
    author_email="<crowxeo@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires = []
    keywords=['python', 'hello', 'crowxeo'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
