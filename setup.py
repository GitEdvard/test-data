from setuptools import setup, find_packages

setup(
    name="test_data",
    version='0.0.1',
    description="Show todays stock winners",
    long_description="Show todays stock winners from a REST API, returning data in json format",
    author="Edvard Englund",
    author_email='edvardenglund@yahoo.se',
    packages=find_packages(include=['test_data', 'test_data.*']),
    include_package_data=True,
    package_data={ '': ['*.csv']},
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'test-data = test_data.cli:start'
        ]
    }
)
