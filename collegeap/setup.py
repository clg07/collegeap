from setuptools import setup, find_packages

setup(
    name='collegeap',  # The name of your package
    version='0.1',  # Initial release version
    description='A simple Python module for college',
    long_description=open('README.md').read(),  # Detailed description from README file
    long_description_content_type='text/markdown',
    author='ap',
    author_email='your.email@example.com',
    url='https://github.com/clg07/collegeap',  # GitHub repository or project homepage
    license='MIT',  # License type
    packages=find_packages(),  # Automatically find package directories
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Python version compatibility
)
