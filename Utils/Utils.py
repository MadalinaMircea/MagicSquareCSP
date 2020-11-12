import networkx as nx
import matplotlib.pyplot as plt


def plot_graph(graph, colors=None):
    if colors is None:
        colors = []
    nx.draw(graph, node_color=colors, with_labels=True)
    plt.show()