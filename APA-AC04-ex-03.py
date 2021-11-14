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

brasil = {
    'Acre': ('Amazonas', 'Rondônia'),
    'Alagoas': ('Bahia', 'Pernambuco', 'Sergipe'),
    'Amapá': ('Pará',),
    'Amazonas': ('Acre', 'Mato Grosso', 'Pará', 'Rondônia', 'Roraima'),
    'Bahia': ("Alagoas", "Espírito Santo", "Goiás", "Minas Gerais", "Pernambuco", "Piauí", "Sergipe", "Tocantins"),
    'Ceará': ('Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte'),
    'Distrito Federal': ('Goiás', 'Minas Gerais'),
    'Espírito Santo': ('Bahia', 'Minas Gerais', 'Rio de Janeiro'),
    'Goiás': ('Bahia', 'Distrito Federal', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Tocantins'),
    'Maranhão': ('Pará', 'Piauí', 'Tocantins'),
    'Mato Grosso': ('Amazonas', 'Goiás', 'Mato Grosso do Sul', 'Pará', 'Rondônia', 'Tocantins'),
    'Mato Grosso do Sul': ('Goiás', 'Mato Grosso', 'Minas Gerais', 'Paraná', 'São Paulo'),
    'Minas Gerais': ('Bahia', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Mato Grosso do Sul', 'Rio de Janeiro', 'São Paulo'),
    'Pará': ('Amapá', 'Amazonas', 'Maranhão', 'Mato Grosso', 'Roraima', 'Tocantins'),
    'Paraíba': ('Ceará', 'Pernambuco', 'Rio Grande do Norte'),
    'Paraná': ('Mato Grosso do Sul', 'Santa Catarina', 'São Paulo'),
    'Pernambuco': ('Alagoas', 'Bahia', 'Ceará', 'Paraíba', 'Piauí'),
    'Piauí': ('Bahia', 'Ceará', 'Maranhão', 'Tocantins'),
    'Rio de Janeiro': ('Espírito Santo', 'Minas Gerais', 'São Paulo'),
    'Rio Grande do Norte': ('Ceará', 'Paraíba'),
    'Rio Grande do Sul': ('Santa Catarina',),
    'Rondônia': ('Acre', 'Amazonas', 'Mato Grosso'),
    'Roraima': ('Amazonas', 'Pará'),
    'Santa Catarina': ('Paraná', 'Rio Grande do Sul'),
    'São Paulo': ('Mato Grosso do Sul', 'Minas Gerais', 'Paraná', 'Rio de Janeiro'),
    'Sergipe': ('Alagoas', 'Bahia'),
    'Tocantins': ('Bahia', 'Goiás', 'Maranhão', 'Mato Grosso', 'Pará', 'Piauí')
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
      grafoparaDesenhar.append((key,ligacoes))
  return grafoparaDesenhar


#terminar
def busca_melhor_cidade_por_profundidade(listacidade):
  for cidade in listacidade:
    buscaP = busca_profundidade(estados,cidade)
  pass



# --------------------------------------------------- main
# tuplas com estados
tuplaEstados = criaTuplaEstados(brasil)
print(tuplaEstados)

# desenha grafo com todas as conexões
desenhaGrafo(tuplaEstados)

# realiza buscas
buscaLarguraEstados = busca_largura(brasil, "Goiás")
buscaProfundidadeEstados = busca_profundidade(brasil, "Goiás")

# desenha grafos
desenhaGrafo(criaTuplaEstados(buscaLarguraEstados))
desenhaGrafo(criaTuplaEstados(buscaProfundidadeEstados))