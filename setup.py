import os

from setuptools import find_packages, setup

base_packages = [
    "numpy",
    "matplotlib",
    "opencv-python>=4.5",
]
test_packages = base_packages + [  # we need extras packages for their tests
    "pytest",
    "black",
    "pylint",
    "pre-commit ",
]
util_packages = [
    "jupyter",
]
dev_packages = test_packages + util_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="puzzlesolver",
    version="0.0.1",
    description="A puzzle solver",
    author="Pim Hoeven",
    packages=find_packages(exclude=["notebooks"]),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    install_requires=base_packages,
    extras_require={
        "base": base_packages,
        "dev": dev_packages,
    },
)
