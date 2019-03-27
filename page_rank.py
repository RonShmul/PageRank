import csv
from node import Node
graph = {}
mapper = {}
page_rank_list = []


def load_graph(path):
    """
    loads csv file and creates 2 dictionaries: mapper which maps node name to node id
    and graph which has the node id as key and Node object as value
    the Node object has a list_of_out which contains all of its destinations (as source node)
    and a list_of_in with all of its sources (as destination node)
    :param path: string
    :return: None
    """
    global graph
    global mapper
    index = 1  # index for id allocation
    with open(path) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            src = str(row[0])
            dest = str(row[1])

            # insert to mapper if not exists and get the source id and destination id
            if src in mapper:
                src_id = mapper[src]
            else:
                src_id = index
                mapper[src] = index
                index += 1

            if dest in mapper:
                dest_id = mapper[dest]
            else:
                dest_id = index
                mapper[dest] = index
                index += 1

            # insert Node object if not exists and insert source id to list_of_in of destination node
            # and insert destination id to list_of_out of source node
            src_node = graph.get(src_id, Node(src))
            graph[src_id] = src_node

            dest_node = graph.get(dest_id, Node(dest))
            graph[dest_id] = dest_node

            src_node.list_of_out.append(dest_id)
            dest_node.list_of_in.append(src_id)


def initial_pr():
    N = len(graph)
    for (key, value) in graph.items():
        value.page_rank = 1/N


def calculate_page_rank(b=0.85, e=0.001):
    global page_rank_list
    initial_pr()
    pr_sum = 0
    iter_num = 0
    first = True
    while (iter_num < 20 and pr_sum > e) or first:
        first = False
        calculate_ranks(b)
        for (key, value) in graph.items():
            pr_sum += abs(value.page_rank - value.prev_pr)
        iter_num += 1
    page_rank_list = sorted(graph.items(), key=lambda kv: kv[1].page_rank, reverse=True)


def calculate_ranks(b):
    S = 0
    for (key, value) in graph.items():
        # update previous page rank- move all current to prev
        value.prev_pr = value.page_rank
        temp_rank = 0
        for node_id in value.list_of_in:
            node = graph[node_id]
            temp_rank += b * (node.prev_pr / len(node.list_of_out))
        value.page_rank = temp_rank
        S += value.page_rank
    factor = (1-S)/len(graph)
    for (key, value) in graph.items():
        value.page_rank += factor


def get_PageRank(node_name):
    """
    get node name and return its pageRank.
    If the name node doesn't exist return -1
    :param node_name: string
    :return pageRank: float
    """
    node_obj = graph.get(mapper.get(node_name, -1), -1)
    if node_obj == -1:
        return -1
    else:
        return node_obj.page_rank


def Get_top_nodes(n):
    """
    Return a list of n nodes sorted by pageRank from high to low.
    The list contains tuples (node name, pageRank value)
    :param n: integer
    :return page_rank_list: list<node_name, pageRank>
    """
    return page_rank_list[:int(n)]


def get_all_PageRank():
    """
    Return a list of all nodes sorted by pageRank from high to low.
    The list contains tuples (node name, pageRank value)
    :return page_rank_list: list<node_name, pageRank>
    """
    return page_rank_list


p = 'Wikipedia_votes.csv'
load_graph(p)
calculate_page_rank()
# print(graph)
# print(get_all_PageRank())
top = Get_top_nodes(4)
