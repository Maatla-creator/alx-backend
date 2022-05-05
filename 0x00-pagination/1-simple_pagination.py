#!/usr/bin/env python3
""" This script implements a method named get_page
that takes two integer arguments page with default value 1
and page_size with default value 10."""


from typing import List
import math
import csv


def index_range(page, page_size):
    """ function index_range takes two integer arguments page and page_size."""
    return ((page - 1) * page_size, (page * page_size))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        ''' init '''
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ function get_page that takes two integer arguments page
        with default value 1 and page_size with default value 10."""
        assert isinstance(page, int) is True and isinstance(
            page_size, int) is True, "values must be int"

        assert page > 0 and page_size > 0, "Value must be positive"

        paged_data = []
        data_set = self.dataset()
        data_set_size = len(data_set)

        ranges = index_range(page, page_size)
        start_index = ranges[0]
        end_index = ranges[1]

        if ranges[0] > data_set_size:
            return []

        for index in range(start_index, end_index):
            paged_data.append(data_set[index])
        return paged_data
