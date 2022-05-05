#!/usr/bin/env python3
""" This script contains a function that returns a tuple of size two
containing a start index and an end index corresponding to the range
of indexes to return in a list for those particular pagination parameters."""


def index_range(page, page_size):
    """ function index_range takes two integer arguments page and page_size."""
    return ((page - 1) * page_size, (page * page_size))
