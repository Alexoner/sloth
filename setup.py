from setuptools import setup, find_packages

setup(
    name         = 'sloth',
    version      = '0.1',
    packages     = find_packages(),
    entry_points = {'sloth': ['settings = sloth.settings']},
)

