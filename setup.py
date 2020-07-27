from setuptools import setup, find_packages


setup(
    author="Unviray",
    author_email="unviray@gmail.com",
    python_requires=">=3.7",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.7',
    ]
    description="Build html component with python",
    license="MIT license",
    keywords="html component react angular vue javascript js nodejs node",
    name="beam",
    packages=find_packages(include=['beam', 'beam.*']),
    url='https://github.com/Unviray/beam',
    version='0.1.0',
    zip_safe=False,
)
