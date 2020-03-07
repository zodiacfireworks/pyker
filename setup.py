#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import find_packages, setup

package_name = "pyker"
package_path = os.path.abspath(os.path.dirname(__file__))
repositorty_url = "https://github.com/zodiacfireworks/pyker"
long_description_file_path = os.path.join(package_path, "README.md")
long_description = ""

try:
    with open(long_description_file_path) as f:
        long_description = f.read()
except IOError:
    pass


setup(
    name=package_name,
    packages=find_packages(exclude=[".*", "docs", "scripts", "tests*"]),
    include_package_data=True,
    version=__import__("pyker").__version__,
    description="""Simple poker game in pure python""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Martin Vuelta",
    author_email="Martin Vuelta <zodiacfireworks@softbutterfly.io>",
    zip_safe=False,
    keywords=["Poker"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    url=repositorty_url,
    # Gitlab url format
    # download_url="%(url)s/-/archive/%(version)s/%(package)s-%(version)s.tar.gz"
    download_url="%(url)s/archive/%(version)s.tar.gz"
    % {
        "url": repositorty_url,
        "version": __import__("pyker").__version__,
        # Required by Gitlab url format
        # "package": package_name,
    },
    requires=[],
    install_requires=[],
)
