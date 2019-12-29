import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wmata",
    version="1.0.0",
    author="Emma K Alexandra",
    author_email="emma@emma.sh",
    description="A simple interface to the WMATA API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emma-k-alexandra/pywmata",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests2'
    ],
    tests_require=[
        'vcrpy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)