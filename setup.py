import os
from setuptools import setup, find_packages

import edxchatbot

install_requires = open('requirements.txt').read().splitlines()

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="edx-chatbot",
    version=edxchatbot.__version__,
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    author='Skillup Tech',
    author_email='dhastha@skillup.tech',
    url="https://github.com/SkillUpTech/edx-chatbot",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires
)
