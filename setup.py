# -*- coding: utf-8 -*-

import os

from setuptools import setup


__here__ = os.path.abspath(os.path.dirname(__file__))


def parse_requiements(stream):
    pass


README = open(os.path.join(__here__, 'README.rst')).read()

# Comment parsing of requirements temporally for development
# REQUIREMENTS = [
#     i.strip()
#     for i in
#     open(os.path.join(__here__, 'requirements', 'dist.txt')).readlines()
# ]
REQUIREMENTS = [
    'candv>=1.3,<1.4',
    'six>=1.6.1',
    'verboselib>=0.2,<0.3',
    'stringlike>=0.3.3',
    'il2fb-commons==0.11.0dev0',
]
DEPENDENCIES = [
    'git+https://github.com/IL2HorusTeam/il2fb-commons.git#egg=il2fb-commons-0.11.0dev0',
]

# Get VERSION
version_file = os.path.join('il2fb', 'config', 'difficulty', 'version.py')
# Use exec for compabibility with Python 3
exec(open(version_file).read())

setup(
    name='il2fb-difficulty',
    version=str(VERSION),
    description="Parser and emitter of difficulty settings for IL-2 FB",
    long_description=README,
    keywords=[
        'il2', 'il-2', 'fb', 'forgotten battles', 'difficulty', 'parser',
        'emitter',
    ],
    license='LGPLv3',
    url='https://github.com/IL2HorusTeam/il2fb-difficulty/',
    author='Alexander Oblovatniy, Alexander Kamyhin',
    author_email='oblovatniy@gmail.com, kamyhin@gmail.com',
    namespace_packages=[
        'il2fb',
        'il2fb.config',
    ],
    packages=[
        'il2fb.config.difficulty',
        'il2fb.config.difficulty.settings',
    ],
    include_package_data=True,
    install_requires=REQUIREMENTS,
    dependency_links=DEPENDENCIES,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ],
    platforms=[
        'any',
    ],
)
