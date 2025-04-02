from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()


    setup(
        name='crop_recommendation_model',
        version='1.0.0',
        discription='This is a recommendation model for crops based on weather data and soil composition.',
        author='Monty vasita',
        author_email='montyvasita1@gmail.com')