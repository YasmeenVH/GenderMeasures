
import networkx as nx

def create_graph(df):
    k = list(df.keys())
    edge_list = []
    weight_list = []
    all_vocab = []

    for x in df:
        vocab_poli = df[x]['words']
        all_vocab.append(vocab_poli)

    flat_list = [item for sublist in all_vocab for item in sublist]
    master_vocab = list(sorted(set(flat_list)))

    for i in range(1, len(df)):
        for j in range(0, len(df[i]['words'])):
            edge = (k[i], df[i]['words'][j])
            weight = (k[i], df[i]['words'][j], df[i]['weight'][j])
            edge_list.append(edge)
            weight_list.append(weight)

    B = nx.Graph()
    B.add_nodes_from(k, bipartite=0)
    B.add_nodes_from(master_vocab, bipartite=1)
    B.add_weighted_edges_from(weight_list)
    print("this graph has: ", len(k), ' number of dataset')
    print("this graph has: ", len(master_vocab), ' number of gendered words words')
    print("this graph has: ", len(edge_list), ' number of edges')
    return k, edge_list, weight_list, B, master_vocab




if __name__ == "__main__":
    data = "./Documents/PHD/GenderMeasures/test-1.csv"
    G = create_graph(data)
    G = nx.Graph()
    # for testing
    G.add_nodes_from([2, 3])

    # get the number of nodes and edges
    G.number_of_nodes(), G.number_of_edges()

    # set an attribute of an edge
    G.add_edge(1, 3)
    G[1][3]['color'] = 'blue'


