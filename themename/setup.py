from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name="mkdocs-themename",
    version=VERSION,
    url='',
    license='',
    description='',
    author='',
    author_email='',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'themename = themename',
        ]
    },
    zip_safe=False
)