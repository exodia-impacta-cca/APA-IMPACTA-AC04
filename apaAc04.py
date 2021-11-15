from networkx.algorithms.distance_measures import periphery
from desenhaGrafo import *
from profundidadeGrafoNetworkx import *


def busca_largura(grafo, primeiro_elemento):
    """grafo: dicionário {elemento: [conexões]}"""
    arvore = dict()
    fila = [primeiro_elemento]
    visitados = set()

    while len(fila) > 0:
        v = fila.pop(0)
        visitados.add(v)

        if v not in arvore.keys():
            arvore[v] = []

        for w in grafo[v]:
            if w not in visitados:
                visitados.add(w)
                fila.append(w)
                arvore[v].append(w)

    return arvore


def busca_profundidade(grafo, primeiro_elemento):
    """grafo: dicionário {elemento: [conexões]}"""
    arvore = dict()
    pilha = [primeiro_elemento]
    visitados = set()

    while len(pilha) > 0:
        v = pilha[-1]
        visitados.add(v)

        if v not in arvore.keys():
            arvore[v] = []

        remover = True
        for w in grafo[v]:
            if w not in visitados:
                visitados.add(w)
                pilha.append(w)
                arvore[v].append(w)
                remover = False
                break

        if remover:
            pilha.pop(-1)

    return arvore


def busca_largura_lista(grafo, primeiro_elemento):
    """grafo: dicionário {elemento: [conexões]}"""
    conexoes = []
    fila = [primeiro_elemento]
    visitados = set()

    while len(fila) > 0:
        v = fila.pop(0)
        visitados.add(v)

        for w in grafo[v]:
            if w not in visitados:
                visitados.add(w)
                fila.append(w)
                conexoes.append((v, w))

    return conexoes


# ------------------------------ Métodos criados pelos alunos


def criaTuplaEstados(dictEstados):
    """recebe dict como argumento e retona lista de conexoes entre vertices"""
    grafoparaDesenhar = []
    for key in dictEstados.keys():
        for ligacoes in dictEstados[key]:
            grafoparaDesenhar.append((key, ligacoes))
    return grafoparaDesenhar


def buscaCaminhoLinear(tuplaEstados):
    # gerar uma arvore de busca minima  com uma key
    valido = False
    for estado in tuplaEstados.keys():
        profundidade = busca_profundidade(tuplaEstados, estado)

        for conexoes in profundidade.items():
            print()
            print(conexoes)
            print()
            
            if len(conexoes[1]) > 1:
    
                valido = False
                break
            else:
                valido = True
      
        if valido:
            
            return profundidade
    
    return None


def buscaCaminhoLinearProfundidade(mapa):
    # gerar uma arvore de busca minima  com uma key
    for estado in mapa.keys():
        print(estado)
        desenhaGrafoComListaDistancia(criaTuplaEstados(busca_profundidade(mapa, estado)))
    

def motraDictPorLinha(dictGrafo):
    """recebe dict como argumento e retona lista de conexoes entre vertices
    em formato de dict"""
    for key in dictGrafo.keys():
        print(f"{key}{dictGrafo[key]}")

def motraDictPorLinha2(dictGrafo):
    """recebe dict como argumento e retona lista de conexoes entre vertices
    em formato de dict"""
    for k,v in dictGrafo.items():
        print(f"{k}{v}")

