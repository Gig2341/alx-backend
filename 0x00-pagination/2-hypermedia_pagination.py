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
        assert isinstance(page, int) and ( page > 0 )
        assert isinstance(page_size, int) and ( page_size > 0 )

        new_set = self.dataset()
        new_index = list(self.index_range(page, page_size))

        return new_set[new_index[0]:new_index[-1]]

    def index_range(self, page: int, page_size: int) -> Tuple:
        '''                                                                         14     this function returns a tuple
        '''
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
         
        return start_index, end_index

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''
        returns a dictionary
        '''
        total_pages = math.ceil(len(self.dataset()) / page_size)
        new_dict = {}
        new_dict['page_size'] = len(self.get_page(page, page_size))
        new_dict['page'] = page
        new_dict['data'] = self.get_page(page, page_size)
        new_dict['next_page'] = min(page + 1, total_pages) if page < total_pages else None
        new_dict['prev_page'] = max(page - 1, 1) if page > 1 else None
        new_dict['total_pages'] = total_pages

        return new_dict
        

