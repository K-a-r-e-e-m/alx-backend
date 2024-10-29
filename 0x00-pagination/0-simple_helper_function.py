#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page, page_size):
    '''return a tuple of size two containing a start index
       and an end index corresponding to the range of indexes
       to return in a list for those particular pagination parameters.'''
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


# Page numbers are 1-indexed ( page = 1 - index )
# if page = 1 ( 1 = 1 - index ) --> (index = page - 1) = (1 - 1) = 0
# Explanation of the Function's Task

# The function takes two inputs:
# page: The page number (starting from 1).
# page_size: The number of items you want to show on each page.

# It returns a tuple containing:
# start_index: The index in the list where this page starts.
# end_index: The index in the list where this page ends.


# For example:
# If page=1 and page_size=10, the function would return (0, 10),
# meaning items from index 0 to index 9 (10 items).

# If page=2 and page_size=10, it would return (10, 20),
# meaning items from index 10 to index 19.
