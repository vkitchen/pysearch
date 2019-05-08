# pysearch

## About

A simple search engine written in python to test whether it was possible to search the wsj collection in less than a second using a high level language.

## Usage

Make sure `wsj.xml` is available in the same directory as `index.py` and `search.py`. Then run `index.py` to build the index. `search.py` takes a line of input from standard in of terms. Performs a query for those terms, prints results and exits.

## Todo

* TFIDF ranking
* Speed improvements? (100s to index, 0.25s to search currently)
