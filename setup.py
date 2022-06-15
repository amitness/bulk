from setuptools import setup, find_packages

setup(
    name="bulk",
    version="0.0.2",
    packages=find_packages(),
    install_requires=["typer>=0.4.1", "bokeh>=2.4.3", "matplotlib>=3.4.2"],
    entry_points={
        'console_scripts': [
            'bulk = bulk.__main__:app',
        ],
    },
)
