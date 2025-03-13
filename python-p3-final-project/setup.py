from setuptools import setup, find_packages

setup(
    name='lib_cli',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'SQLAlchemy',
        'alembic',
    ],
    entry_points={
        'console_scripts': [
            'lib-cli=lib_cli:cli',
        ],
    },
)