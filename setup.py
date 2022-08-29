from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="creak_sense",
    version="0.0.2",
    url="http://github.com/fractalego/creak_sense",
    author="Alberto Cetoli",
    author_email="alberto@fractalego.io",
    description="Tests whether a sentence is consistent with the CREAK dataset.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[
        "creak_sense",
    ],
    install_requires=[
        "transformers==4.17.0",
        "sentence_transformers==2.0.0",
        "torch==1.9.0",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True,
    zip_safe=False,
)
