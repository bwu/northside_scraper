import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='northside_scraper',
    version='0.0.1',
    author='Brian Wu',
    author_email='brian.george.wu@gmail.com',
    url='https://github.com/bwu/northside_scraper',
    description='Scrape artists and make playlists',
    keywords=['spotify'],
    packages=['northside_scraper'],
    install_requires=['spotipy'],
    include_package_data = True
)
