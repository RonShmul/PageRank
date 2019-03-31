class Node:
    def __init__(self, name):
        self.name = name
        self.list_of_in = []
        self.list_of_out = []
        self.page_rank = 0
        self.prev_pr = 0
