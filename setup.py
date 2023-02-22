from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Short package description.'
LONG_DESCRIPTION = 'Longer package description.'


setup(
    name='package',
    packages=find_packages(include=['mypackage']),
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Full name',
    license='MIT',
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'requests',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
    ],
)
