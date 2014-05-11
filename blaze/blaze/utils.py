from itertools import islice
from contextlib import contextmanager
import tempfile
import os


def partition_all(n, seq):
    """ Split sequence into subsequences of size ``n``

    >>> list(partition_all(3, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

    The last element of the list may have fewer than ``n`` elements

    >>> list(partition_all(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10,)]
    """
    seq = iter(seq)
    while True:
        result = tuple(islice(seq, 0, n))
        if result:
            yield result
        else:
            raise StopIteration()


def nth(n, seq):
    """

    >>> nth(1, 'Hello, world!')
    'e'
    >>> nth(4, 'Hello, world!')
    'o'
    """
    seq = iter(seq)
    i = 0
    while i < n:
        i += 1
        next(seq)
    return next(seq)


@contextmanager
def filetext(text, extension='', open=open):
    with tmpfile(extension=extension) as filename:
        with open(filename, "w") as f:
            f.write(text)

        yield filename


@contextmanager
def filetexts(d, open=open):
    """ Dumps a number of textfiles to disk

    d - dict
        a mapping from filename to text like {'a.csv': '1,1\n2,2'}
    """
    for filename, text in d.items():
        with open(filename, 'w') as f:
            f.write(text)

    yield list(d)

    for filename in d:
        if os.path.exists(filename):
            os.remove(filename)


@contextmanager
def tmpfile(extension=''):
    filename = tempfile.mktemp(extension)

    yield filename

    if os.path.exists(filename):
        os.remove(filename)


def raises(err, lamda):
    try:
        lamda()
        return False
    except err:
        return True
