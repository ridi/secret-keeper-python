
"""A setuptools based setup module.
"""

from setuptools import setup, find_packages

setup(
    name='secret-keeper',
    packages=[
        'ridi.secret_keeper',
    ],
    version='0.3.0a2',
    description='Secret Keeper',
    url='https://github.com/ridi/secret-keeper-python',
    keywords=['secret', 'secret-keeper', 'ridi', 'ridibooks'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'boto3>=1.9.16',
    ],
    entry_points={
        'console_scripts': [
            'secret-keeper = ridi.secret_keeper.cmdline:main'
        ]
    },
)
