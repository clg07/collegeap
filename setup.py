from setuptools import setup

setup(
    name="collageap",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A brief description of your module",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    py_modules=["collageap"],  # This matches the name of your Python file (collageap.py)
    url="https://github.com/yourusername/collageap",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
