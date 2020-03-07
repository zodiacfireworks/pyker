# Pyker

Simple pker game in pure python

## what to do with this library?

For now I just implmented an algorithm for ranking poker hands based on the description given here
http://nsayer.blogspot.com/2007/07/algorithm-for-evaluating-poker-hands.html

Please check `samples/Comparsion.ipynb` to se how it works

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
