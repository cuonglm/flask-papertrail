import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import flask_papertrail


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='Flask-PaperTrail',
    packages=['flask_papertrail'],
    version=flask_papertrail.__version__,
    description='Adds PaperTrail logging to your Flask application',
    long_description=read('README.rst'),
    author=flask_papertrail.__author__,
    author_email=flask_papertrail.__email__,
    license='BSD',
    url='https://github.com/Gnouc/flask_papertrail',
    keywords=['flask', 'log'],
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
