#!/usr/bin/env python3
"""Hypermedia pagination"""
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    '''return a tuple of size two containing a start index
       and an end index corresponding to the range of indexes
       to return in a list for those particular pagination parameters.'''
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        """Returns the data of page using index_range function"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        data = self.dataset()
        return data[start_idx:end_idx]  # Using Slicing
        # return [data[i] for i in range(start_idx, end_idx) if i < len(data)]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary containing some key-value pairs"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        total_page = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": (page + 1) if page < total_page else None,
            "prev_page": (page - 1) if page != 1 else None,
            "total_pages": total_page
        }
