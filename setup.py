from setuptools import setup, find_packages

setup(
    name='il2ds-difficulty',
    version='1.0.0',
    description='Convert integer value of IL-2 DS difficulty into ' \
                'informative dictionary.',
    license='BSD License',
    url='https://github.com/IL2HorusTeam/il2ds-difficulty/',
    author='Alexander Oblovatniy',
    author_email='oblovatniy@gmail.com',
    packages=find_packages(),
    install_requires=[i.strip() for i in open("requirements.pip").readlines()],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Environment :: Console',
        'License :: Free for non-commercial use',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Framework :: Django',
    ],
)
