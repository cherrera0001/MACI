from setuptools import setup

setup(
    name="maci-herramientas",
    version="1.0.0",
    description="MACI tools and scripts",
    packages=["herramientas"],
    python_requires=">=3.9",
    install_requires=[
        "PyYAML",
        "playwright",
    ],
)
