# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "bellhop-python-sdk"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

# read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

REQUIRES = [
    "certifi >= 2023.7.22",
    "python-dateutil ~= 2.8.2",
    "typing_extensions ~= 4.3.0",
    "urllib3 ~= 1.26.18",
    "cryptography ~= 41.0.6",
    "frozendict ~= 2.3.4",
    "aiohttp ~= 3.9.1",
    "pydantic ~= 2.4.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="OpenAPI Petstore",
    author="Konfig",
    author_email="engineering@konfigthis.com",
    url="https://github.com/konfig-dev/bellhop-sdks/tree/main/python",
    keywords=["Konfig", "OpenAPI Petstore"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache-2.0",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
