#!/usr/bin/env python3

"""Return a tuple containing start and end indexes for a page of data."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a page of data.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
        and end index (exclusive) for slicing.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
