#!/usr/bin/env python3
""" index_range that takes two integer arguments
page and page_size module """


def index_range(page, page_size):
    """ index range function """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
