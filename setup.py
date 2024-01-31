from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Short package description."
with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()


setup(
    name="package",
    packages=find_packages(include=["mypackage"]),
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Full name",
    license="MIT",
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
        "requests",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
    ],
)
