#!/usr/bin/env python3
""" Module fir Server class """
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """ index range function """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """ Return a list of page rows """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        dataset = self.dataset()
        try:
            limits = index_range(page, page_size)
            return dataset[limits[0]:limits[1]]
        except Exception:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ method that returns a dictionary
        containing the specific key-value pairs """
        data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size
        values = {
            "page_size": page_size if page_size <= len(data) else len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page >= 0 else None,
            "prev_page": page - 1 if page >= 1 else None,
            "total_pages": total_pages
            }
        return values
