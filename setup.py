import os
from setuptools import setup

setup(
    name="collageap",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A brief description of your module",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    py_modules=["collageap"],
    url="https://github.com/clg07/collageap",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
