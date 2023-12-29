#!/usr/bin/env python3

'''
this module  return a tuple of size two containing a start index and an end
index corresponding to the range of indexes to return in a list for thos
e particular pagination parameters.
'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''
    this function returns a tuple
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
