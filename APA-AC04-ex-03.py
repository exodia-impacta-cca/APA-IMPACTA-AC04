from networkx.algorithms.distance_measures import periphery
from desenhaGrafo import *

estados = {

    'RR': ['AM','PA'],
    'AM': ['AC','RO','PA','MT','RR'],
    'AC': ['AM','RO'],
    'RO': ['AC','AM','MT'],
    'PA': ['AP','AM','TO','MT','RR','MA'],
    'AP': ['AP'],
    'MT': ['AM','PA','RO','TO','GO','MS'],
    'TO': ['PA','PI','MA','MT','BA','GO'],
    'MS': ['GO','MG','SP','PR'],
    'PR': ['MS','SP','SC'],
    'SC': ['PR','RS'],
    'RS': ['SC'],
    'SP': ['PR','MS','RJ','MG'],
    'RJ': ['ES','SP','MG'],
    'ES': ['RJ','MG','BA'],
    'MG': ['ES','RJ','SP','MS','GO','BA'],
    'GO': ['MT','MS','TO','MG','BA'],
    'BA': ['SE','AL','TO','PE','PI','GO'],
    'SE': ['BA','AL'],
    'AL': ['PE','SE','BA'],
    'PE': ['AL','BA','PB','CE','PI'],
    'PB': ['RN','CE','PE'],
    'RN': ['PB','CE'],
    'CE': ['RN','PB','PE','PI'],
    'PI': ['CE','MA','PE','BA','TO'],
    'MA': ['PI','TO','PA'],
    
}

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

melhorEstado= []
conexoes = 0
for estado in estados.items():

    if(len(estado[1]) > conexoes):
        conexoes = len(estado[1])
        melhorEstado = estado

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

def busca_melhor_cidade_por_profundidade(listacidade):
  for cidade in listacidade:
    buscaP = busca_profundidade(estados,cidade)

def criaTuplaEstados(dictEstados):
  grafoparaDesenhar = []
  for key in dictEstados.keys():
    for ligacoes in dictEstados[key]:
      grafoparaDesenhar.append((key,ligacoes))
  return grafoparaDesenhar
    

buscaP = busca_profundidade(estados,'TO')
buscaL = busca_largura(estados,'TO')

A = criaTuplaEstados(buscaP)    
B = criaTuplaEstados(buscaL)
print(buscaP)

tamanhoBuscaProfundidade=desenhaGrafo(A)
tamanhoBuscaLargura=desenhaGrafo(B)

print(tamanhoBuscaLargura)
print()
print(tamanhoBuscaProfundidade)

# print("Busca de profundidade: ")
# print(buscaP)

# print("Busca em Largura:")
# print(buscaL)