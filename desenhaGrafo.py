import networkx as nx
import matplotlib.pyplot as plt

def desenhaGrafoComListaDistancia(listaCidadeDistancia):
    g = nx.Graph()
    for edge in listaCidadeDistancia:
        g.add_edge(edge[0], edge[1])
    nx.draw_networkx(g)
    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.15)
    plt.axis("off")
    plt.show()

def desenhaGrafo(g):
    nx.draw_networkx(g)
    ax = plt.gca()
    ax.margins(0.15)
    plt.axis("off")
    plt.show()

def criaTuplaEstados(dictEstados):
    """recebe dict como argumento e retona lista de conexoes entre vertices"""
    grafoparaDesenhar = []
    for key in dictEstados.keys():
        for ligacoes in dictEstados[key]:
            grafoparaDesenhar.append((key, ligacoes))
    return grafoparaDesenhar

def criaGrafoNextowrkXComEdges(listaCidadeDistancia):
    G = nx.Graph()
    for edge in listaCidadeDistancia:
        G.add_edge(edge[0], edge[1])
    return G


def criaGrafoNextowrkXComNodes(listaCidadeDistancia):
    G = nx.Graph()
    G.add_nodes_from(listaCidadeDistancia)
    G.add_edges_from(criaTuplaEstados(listaCidadeDistancia))
    return G
 