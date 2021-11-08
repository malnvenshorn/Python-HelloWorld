from setuptools import setup, find_packages

setup(
    name='hello_world',
    version='0.4.0',
    description='say hello in python',
    url='https://github.com/malnvenshorn/python-hello-world',
    author='malnvenshorn',
    author_email='malnvenshorn@mailbox.org',
    license='GPLv3',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
)
