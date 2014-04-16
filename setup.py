from setuptools import setup, find_packages

setup(
    name='il2-difficulty',
    version='1.1.0',
    description='Convert integer value of IL-2 difficulty into ' \
                'informative dictionary.',
    license='GPLv2',
    url='https://github.com/IL2HorusTeam/il2-difficulty/',
    author='Alexander Oblovatniy, Alexander Kamyhin',
    author_email='oblovatniy@gmail.com, kamyhin@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[i.strip() for i in open("requirements.pip").readlines()],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'License :: Free for non-commercial use',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
    ],
)
