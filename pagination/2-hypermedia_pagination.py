#!/usr/bin/env python3
"""Hypermedia pagination over Popular_Baby_Names.csv."""

import csv
import math
import os
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = os.path.join(
        os.path.dirname(__file__),
        "Popular_Baby_Names.csv"
    )

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
        Retrieve a specific page of the dataset.

        Args:
            page (int): The page number to return. Must be a positive
            page_size (int): The number of items per page. Must be a positive

        Returns:
            List[List]: The rows of the dataset for the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Return a dictionary with pagination metadata and the page of data.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),      # actual number of items returned
            "page": page,                # current page number
            "data": data,                 # actual rows for this page
            "next_page": next_page,       # next page number or None
            "prev_page": prev_page,       # previous page number or None
            "total_pages": total_pages    # total number of pages
        }
