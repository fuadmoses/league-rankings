from setuptools import setup

version = open("version").read().strip()

setup(
   name='league_rankings',
   version=version,
   description='A League Ranking Calculator',
   author='Fuad Moses',
   author_email='fuadmoses@gmail.com',
   url='https://github.com/fuadmoses/league-rankings',
   packages=['league_rankings'],
)
