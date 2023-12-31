import os.path as osp
import re
import sys

from setuptools import setup


def find_version():
    with open(osp.join("src", "__init__.py"), "r") as f:
        match = re.search(r'^__version__ = "v(\d+\.\d+\.\d+)"', f.read(), re.M)
        if match is not None:
            return match.group(1)
        raise RuntimeError("Unable to find version string.")


def get_readme_content():
    basedir = osp.dirname(osp.realpath(sys.argv[0]))
    with open(osp.join(basedir, "README.md"), "r") as f:
        content = f.read()
    return content


setup(
    name="rapid_rift_api",
    version=find_version(),
    author="Ebad Kamil",
    author_email="kamilebad@gmail.com",
    description="Rapid Rift API",
    long_description=get_readme_content(),
    long_description_content_type="text/markdown",
    install_requires=[
        "fastapi",
        "uvicorn",
        "sqlmodel",
        "pyyaml",
        "cx_oracle"
        ],
    extras_require={
        "test": [
            "pytest",
            "black==22.3.0",
            "flake8==3.8.4",
            "isort==5.7.0",
        ]
    },
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)