#!/usr/bin/env python

from setuptools import find_packages, setup


with open("README.md") as fp:
    long_description = fp.read()

with open("requirements.txt") as _file:
    install_reqs = []
    dependency_links = []
    for req in _file.readlines():

        if req.startswith("--extra-index-url"):
            dependency_links.append(req.replace("--extra-index-url ", ""))
        else:
            install_reqs.append(req)

with open("tests/requirements.txt") as _file:
    test_reqs = [req for req in _file.readlines()]

setuptools.setup(
    name="lit_telegram",
    version="0.0.1",
    description="Messaging notifications for telegram.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Krishna Kalyan",
    author_email="krishna@grid.ai",
    url="https://github.com/PyTorchLightning/LAI-telegram-messenger",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=install_reqs,
    dependency_links=dependency_links,
    extras_require={
        "test": test_reqs,
    },
    python_requires=">=3.7",
)