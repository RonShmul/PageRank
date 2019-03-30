import csv
import page_rank as pr


def from_reddit(path):
    with open(path, 'r') as txtFile, open('reddit.csv', 'w', newline='') as csvFile:
        csv_writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        lines = txtFile.readlines()
        for edge in lines:
            k, v, w = edge.split('\t')
            csv_writer.writerow([str(k), str(v)])


def from_twitter(path):
    with open(path, 'r') as txtFile, open('twitterWeights.csv', 'w', newline='') as csvFile:
        csv_writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        lines = txtFile.readlines()
        for idx, edge in enumerate(lines):
            k, v, w = edge.split(',')
            w = int(w.replace('\n', ''))
            csv_writer.writerow([str(k), str(v), w])
            if idx > 3000:
                break


def get_top_10_from_file(path):
    pr.load_graph(path)
    pr.calculate_page_rank()
    list_of_nodes = pr.Get_top_nodes(10)
    print(path)
    [print(elem) for elem in list_of_nodes]


def shrink_graph(path_graph, path_csv, n):
    print('start loading..')
    pr.load_graph(path_graph)
    print('start calculating page rank..')
    pr.calculate_page_rank()
    print('get top 10..')
    top = pr.Get_top_nodes(10)
    print('start making the file..')
    nodes = set()
    for node in top:
        print(node)
        add_nodes(nodes, node[0], n)

    with open(path_csv, 'w', newline='') as csvFile:
        csv_writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for edge in nodes:
            csv_writer.writerow([edge[0], edge[1]])


def add_nodes(nodes, node, n):
    if n <= 0:
        return
    node_obj = pr.graph[pr.mapper[node]]
    in_list = node_obj.list_of_in
    out_list = node_obj.list_of_out

    for nb in in_list[:10]:
        nodes.add((pr.graph[nb].name, node))
    for nb in out_list[:10]:
        nodes.add((node, pr.graph[nb].name))

    for nb in in_list[:10]:
        add_nodes(nodes, pr.graph[nb].name, n - 1)

    for nb in out_list[:10]:
        add_nodes(nodes, pr.graph[nb].name, n - 1)


# shrink_graph('twitter.csv', 'twitter.csv', 4)

get_top_10_from_file('Wikipedia_votes.csv')
get_top_10_from_file('reddit.csv')
get_top_10_from_file('twitter.csv')
