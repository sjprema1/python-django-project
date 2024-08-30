import math

class Pagination:

    def __init__(self):
        self.page_no = 1
        self.no_of_rows = 10
        self.limit = 0
        self.offset = 0
        self.total_pages = 1

    def get_offsets(self,page_no):
        self.page_no = int(page_no)
        self.offset = (self.page_no - 1)*self.no_of_rows
        self.limit = self.no_of_rows

    def get_paginator(self,total_records):
        row_count = 0

        if total_records and total_records > 0:
            self.total_pages = math.ceil( int(total_records)/self.no_of_rows)

            if self.page_no == self.total_pages:
                row_count = int(total_records) - ( (self.page_no-1)*self.no_of_rows)
            else:
                row_count = self.no_of_rows

        pagination = {}
        pagination['page_no'] = self.page_no
        pagination['no_of_pages'] = self.total_pages
        pagination['row_count'] = row_count

        return pagination
