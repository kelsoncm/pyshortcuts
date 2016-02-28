# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name='django_brfied',
    packages=['django_brfied',
              'django_brfied.static',
              'django_brfied.static.js',
              'python_brfied', ],
    version='0.1.0',
    description='Django Application specific brazilian fields types',
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    url='https://github.com/kelsoncm/django_brfied', 
    download_url='https://github.com/kelsoncm/django_brfied/releases/tag/1.0.0',
    keywords=['django', 'BR', 'Brazil', 'Brasil', 'model', 'form', 'locale', ],
    classifiers=[]
)
