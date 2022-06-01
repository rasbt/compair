# Sebastian Raschka 2018-2022
# compair model evaluation tools
# Author: Sebastian Raschka <sebastianraschka.com>
#
# License: BSD 3 clause

from os.path import realpath, dirname, join
from setuptools import setup, find_packages
import compair

VERSION = compair.__version__
PROJECT_ROOT = dirname(realpath(__file__))

REQUIREMENTS_FILE = join(PROJECT_ROOT, "requirements.txt")

with open(REQUIREMENTS_FILE) as f:
    install_reqs = f.read().splitlines()

install_reqs.append("setuptools")


setup(
    name="compair",
    version=VERSION,
    description="Machine Learning Library Extensions",
    author="Sebastian Raschka",
    author_email="mail@sebastianraschka.com",
    url="https://github.com/rasbt/compair",
    packages=find_packages(),
    package_data={
        "": ["LICENSE.txt", "README.md", "requirements.txt"]
    },
    include_package_data=True,
    install_requires=install_reqs,
    extras_require={"testing": ["pytest"], "docs": ["mkdocs"]},
    license="BSD 3-Clause",
    platforms="any",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],
    long_description="""

A library of Python tools and extensions for data science.


Contact
=============

If you have any questions or comments about compair,
please feel free to contact me via the issue tracker or
discussion board at
https://github.com/rasbt/compair

""",
)
