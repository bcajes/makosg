from setuptools import setup, find_packages

setup(
    name='makosg',
    version='0.0.1',
    author='Brian Cajes',
    author_email='brian.cajes@gmail.com',
    packages=find_packages(),
    url='https://github.com/bcajes/makosg/',
    license='LICENSE.txt',
    install_requires=['sendgrid-python', 'mako'],
    description='makosg makes rendering rich html for sendgrid emails easier',
    long_description='Works in conjunction with sendgrid-python.  Given mako templated text, some variables, and/or mako files, render richer email content easily.',
)
