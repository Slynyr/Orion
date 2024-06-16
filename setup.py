from setuptools import setup, find_packages

setup(
    name="Orion",
    version="1.0", 
    packages=find_packages(),
    install_requires=["colorama"],
    entry_points={
        "console_scripts": [
            "orion = orion.__main__:mainEntryPoint"
        ]
    }
)