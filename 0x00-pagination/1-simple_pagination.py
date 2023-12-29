#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple


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
        '''
        gets the page
        '''
        assert isinstance(page, int) and (page > 0)
        assert isinstance(page_size, int) and (page_size > 0)

        new_set = self.dataset()
        new_index = list(self.index_range(page, page_size))

        return new_set[new_index[0]:new_index[-1]]

    def index_range(self, page: int, page_size: int) -> Tuple:
        '''
        this function returns a tuple
        '''
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index
