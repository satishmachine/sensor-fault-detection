from setuptools import find_packages,setup

setup(
       name="sensor",
       version="0.0.1",
       author="satish kumar",
       author_email="satishkumar8055@gmail.com",
       packages= find_packages(),
       install_requires=['pymongo==4.3.2'],
)
     