from setuptools import setup

with open('README.md', 'r') as file:
     long_description = file.read()

setup(
    name='randompassword_generator',
    version='1.0',
    description='A package that generates random passwords. ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['randompassword_generator'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    install_requires=['random', 'array'],
    url="https://github.com/shyamgopal01/randompassword_generator",
    author='Shyam Gopal , Venkateswar.S',
    author_email='shyamgopalit@gmail.com'
)