import networkx as nx
import matplotlib.pyplot as plt

def desenhaGrafo(listaCidadeDistancia):
    g = nx.Graph()
    for edge in listaCidadeDistancia:
        g.add_edge(edge[0], edge[1])
    nx.draw_networkx(g)
    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.15)
    plt.axis("off")
    plt.show()


def criaGrafoNextowrkX(listaCidadeDistancia):
    G = nx.Graph()
    for edge in listaCidadeDistancia:
        G.add_edge(edge[0], edge[1])
    return 
 