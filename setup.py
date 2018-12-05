
"""A setuptools based setup module.
"""

from setuptools import setup, find_packages

setup(
    name='secret-keeper',
    packages=[
        'ridi.secret_keeper',
    ],
    version='0.3.0.post1',
    description='Secret Keeper',
    url='https://github.com/ridi/secret-keeper-python',
    keywords=['secret', 'secret-keeper', 'ridi', 'ridibooks'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
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
