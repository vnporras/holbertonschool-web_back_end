#!/usr/bin/env python3
"""
Hypermedia pagination
"""


import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page, page_size) -> Tuple[int, int]:
    """
    The function should return a tuple of size two containing
    a start index and anend index corresponding to the range of
    indexes to return in a list for those particular pagination
    parameters.

    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


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
        """
        Retrieves a page of data from the dataset.

        Args:
            page (int): The page number to retrieve, must be greater than 0.
            page_size (int): The number of items per page,
            must be greater than 0.

        Returns:
            List[List]: A list of rows for the requested page.
            Returns an empty list if the page is out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return pagination details as a dictionary.

        Args:
            page (int): The current page number (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            Dict[str, Any]: A dictionary containing pagination details:
                - 'page_size': Number of items on the current page.
                - 'page': Current page number.
                - 'data': List of items on the current page.
                - 'next_page': Page number of the next page,
                or None if on the last page.
                - 'prev_page': Page number of the previous page,
                or None if on the first page.
                - 'total_pages': Total number of pages.
        """

        data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
