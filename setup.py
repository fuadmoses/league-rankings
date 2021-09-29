from setuptools import setup, find_packages

version = open("version").read().strip()

setup(
   name='league_rankings',
   version=version,
   description='A League Ranking Calculator',
   author='Fuad Moses',
   author_email='fuadmoses@gmail.com',
   url='https://github.com/fuadmoses/league-rankings',
   packages=find_packages(),
   entry_points={
        'console_scripts': [
            'league_rankings = league_rankings.__main__:main'
        ]
    }
)
