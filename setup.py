import os

from setuptools import find_packages, setup

from templater import __version__


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return open(path, encoding='utf-8').read()


setup(
    name="templater",
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    zip_safe=True,

    author="Unviray",
    author_email="unviray@gmail.com",
    description="Build html component with python",
    long_description=read('README.rst'),
    license="MIT license",
    keywords="html component react angular vue javascript js nodejs node",
    url="https://github.com/Unviray/templater",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
