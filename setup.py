"""
Setup the package.
"""
from setuptools import (
    find_packages,
    setup,
)


with open('README.md', 'r') as read_me:
    long_description = read_me.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    version='0.4.0',
    name='remme-core-cli',
    description='The command-line interface (CLI) that provides a set of commands to interact with Remme-core.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Remmeauth/remme-core-cli',
    license='MIT',
    author='Remme',
    author_email='developers@remme.io',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'remme = cli.entrypoint:cli',
        ],
    },
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
