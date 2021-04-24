#!/usr/bin/python

import creole

config = dict(
    name='creole',
    version=creole.__version__,
    url='https://oink.sheep.art.pl/Wiki%20Creole%20Parser%20in%20Python',
    download_url=('http://oink.sheep.art.pl/+download/creole-%s.tar.gz'  # FIXME <<
                  % creole.__version__),
    license='GNU General Public License (GPL), BSD',
    author='Radomir Dopieralski, Thomas Waldmann, Oleksandr Komarov',
    author_email='creole@sheep.art.pl',
    description='Parser for WikiCreole text markup.',
    long_description=creole.__doc__,
    keywords='wiki wikicreole creole markup text',
    packages=['creole'],
    data_files=[
        ('share/doc/creole.py/examples',
         ['examples/creole2html.py', 'examples/headings.py']),
        ('share/doc/creole.py/tests', ['tests/test_html_emitter.py']),
        ('share/doc/creole.py', ['COPYING']),
    ],
    scripts=['examples/creole2html.py'],
    platforms='any',
    classifiers=[
        'Topic :: Text Processing :: Markup',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Intended Audience :: Developers',
        'Topic :: Communications',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
)

from distutils.core import setup
setup(**config)

