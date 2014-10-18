# -*- coding: utf-8 -*-

import os

from setuptools import setup


__here__ = os.path.abspath(os.path.dirname(__file__))

README = open(os.path.join(__here__, 'README.rst')).read()
REQUIREMENTS = [
    i.strip()
    for i in open(os.path.join(__here__, 'requirements.txt')).readlines()
]

setup(
    name='il2fb-difficulty',
    version='1.1.1',
    description="Parser and emitter of difficulty settings for IL-2 FB",
    long_description=README,
    license='LGPLv3',
    url='https://github.com/IL2HorusTeam/il2fb-difficulty/',
    author='Alexander Oblovatniy, Alexander Kamyhin',
    author_email='oblovatniy@gmail.com, kamyhin@gmail.com',
    packages=[
        'il2fb.difficulty',
        'il2fb.difficulty.settings',
    ],
    namespace_packages=[
        'il2fb',
    ],
    include_package_data=True,
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries',
    ],
    platforms=[
        'any',
    ],
)
