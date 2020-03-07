[![Python Versions](https://img.shields.io/pypi/pyversions/pyker.svg?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)
[![PyPI Version](https://img.shields.io/pypi/v/pyker.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/pyker/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pyker.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/pyker/)

[![Build Status](https://travis-ci.org/zodiacfireworks/pyker.svg?branch=master)](https://travis-ci.org/zodiacfireworks/pyker)
[![codecov](https://codecov.io/gh/zodiacfireworks/pyker/branch/master/graph/badge.svg)](https://codecov.io/gh/zodiacfireworks/pyker)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1787644ed8524433b9466f74d24b44d2)](https://www.codacy.com/gh/zodiacfireworks/pyker?utm_source=github.com&utm_medium=referral&utm_content=zodiacfireworks/pyker&utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/1787644ed8524433b9466f74d24b44d2)](https://www.codacy.com/gh/zodiacfireworks/pyker?utm_source=github.com&utm_medium=referral&utm_content=zodiacfireworks/pyker&utm_campaign=Badge_Coverage)
[![Requirements Status](https://requires.io/github/zodiacfireworks/pyker/requirements.svg?branch=master)](https://requires.io/github/zodiacfireworks/pyker/requirements/?branch=master)

[![Stars](https://img.shields.io/github/stars/zodiacfireworks/pyker?logo=github)](https://github.com/zodiacfireworks/pyker/)
[![License](https://img.shields.io/pypi/l/pyker.svg?color=blue)](https://github.com/zodiacfireworks/pyker/blob/master/LICENSE.txt)

# Pyker

Simple poker game in pure python

## what to do with this library?

For now I just implmented an algorithm for ranking poker hands based on the description given here

> http://nsayer.blogspot.com/2007/07/algorithm-for-evaluating-poker-hands.html

Please check `samples/Comparsion.ipynb` to se how it works

## How to install

You can install with pip

```
pip install pyker
```

## How to test

### Requirements

To test you need `poetry` and `pyenv` with `python 3.7` and `python 3.8`, then follow the comands

```
git clone https://github.com/zodiacfireworks/pyker.git
cd pyker
poetry install
poetry run tox
```

And thats all!
