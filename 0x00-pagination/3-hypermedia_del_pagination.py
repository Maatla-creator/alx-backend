#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """get_hyper_index method with two integer arguments:
        index with a None default value and page_size
        with default value of 10."""

        data = []

        indexed_dataset = self.indexed_dataset()
        indexed_dataset_size = len(indexed_dataset)

        assert isinstance(index, int) and index < (indexed_dataset_size - 1)

        i = 0
        j = index
        while (i < page_size and index < indexed_dataset_size):
            val = indexed_dataset.get(j, None)
            if val:
                data.append(val)
                i += 1
            j += 1

        next_index = 0
        while (j < indexed_dataset_size):
            val = indexed_dataset.get(j, None)
            if val:
                next_index = j
                break
            j += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
