class Node:
    def __init__(self, name):
        self.name = name
        self.list_of_in = []
        self.list_of_out = []
        self.page_rank = 0
        self.prev_pr = 0

    def update_page_rank(self, n, beta):
        pass

    def calculate_page_rank(self, b):
        temp_rank = 0
        if len(self.list_of_in) > 0:
            for node in self.list_of_in:
                temp_rank += b * (node.prev_pr / len(node.list_of_out))
        return temp_rank
