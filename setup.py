import os
from setuptools import setup

#install_requires = ["requests"]

base_dir = os.path.dirname(os.path.abspath(__file__))

setup(
    name = "gol",
    version = "0.0.1.dev",
    description = "Learning python by the gameoflife",   
    author = "Erik Almqvist",
    author_email = "erija952@gmail.com",
    packages = ["gol"],
#    zip_safe = False,
    #install_requires = install_requires,
    test_suite = "tests.get_tests",
)
