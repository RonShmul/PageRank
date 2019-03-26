import pandas as pd


def load_graph(path):
    df = pd.read_csv(path)
    df.tostring()  # check if needs?
    # needs to think about the best way to save the edges- maybe a dictionary: for each node the list of nodes which have a connection to it


def calculate_page_rank():
    pass


def get_PageRank(node_name):
    pass


def Get_top_nodes(n):
    pass


def get_all_PageRank():
    pass


"""
from bisect import bisect
data = []
for x in range(0,len(df[0])):
    a,b = randint(1,10),randint(1,100)
    data.insert(bisect(data,(a,1000)),(a,b))
"""