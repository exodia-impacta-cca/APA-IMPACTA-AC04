def desenhaGrafo(listaCidadeDistancia):
    import networkx as nx
    import matplotlib.pyplot as plt

    g = nx.Graph()
    

    for edge in listaCidadeDistancia:
        g.add_edge(edge[0], edge[1])

    
    options = {
        "font_size": 36,
        "node_size": 3000,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 5,
        "width": 5,
    }
    # nx.draw_networkx(G, pos, **options)
    nx.draw_networkx(g, **options)
    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.05)
    plt.axis("off")
    plt.show()

 