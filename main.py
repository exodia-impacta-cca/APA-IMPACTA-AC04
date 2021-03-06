from apaAc04 import *
from desenhaGrafo import *
from profundidadeGrafoNetworkx import *
import networkx as nx

# ------------------------------- dicionario estados Brasil
estados = {
    "RR": ["AM", "PA"],
    "AM": ["AC", "RO", "PA", "MT", "RR"],
    "AC": ["AM", "RO"],
    "RO": ["AC", "AM", "MT"],
    "PA": ["AP", "AM", "TO", "MT", "RR", "MA"],
    "AP": ["AP"],
    "MT": ["AM", "PA", "RO", "TO", "GO", "MS"],
    "TO": ["PA", "PI", "MA", "MT", "BA", "GO"],
    "MS": ["GO", "MG", "SP", "PR"],
    "PR": ["MS", "SP", "SC"],
    "SC": ["PR", "RS"],
    "RS": ["SC"],
    "SP": ["PR", "MS", "RJ", "MG"],
    "RJ": ["ES", "SP", "MG"],
    "ES": ["RJ", "MG", "BA"],
    "MG": ["ES", "RJ", "SP", "MS", "GO", "BA"],
    "GO": ["MT", "MS", "TO", "MG", "BA"],
    "BA": ["SE", "AL", "TO", "PE", "PI", "GO"],
    "SE": ["BA", "AL"],
    "AL": ["PE", "SE", "BA"],
    "PE": ["AL", "BA", "PB", "CE", "PI"],
    "PB": ["RN", "CE", "PE"],
    "RN": ["PB", "CE"],
    "CE": ["RN", "PB", "PE", "PI"],
    "PI": ["CE", "MA", "PE", "BA", "TO"],
    "MA": ["PI", "TO", "PA"],
}

brasil = {
    "Acre": ("Amazonas", "Rondônia"),
    "Alagoas": ("Bahia", "Pernambuco", "Sergipe"),
    "Amapá": ("Pará",),
    "Amazonas": ("Acre", "Mato Grosso", "Pará", "Rondônia", "Roraima"),
    "Bahia": (
        "Alagoas",
        "Espírito Santo",
        "Goiás",
        "Minas Gerais",
        "Pernambuco",
        "Piauí",
        "Sergipe",
        "Tocantins",
    ),
    "Ceará": ("Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte"),
    "Distrito Federal": ("Goiás", "Minas Gerais"),
    "Espírito Santo": ("Bahia", "Minas Gerais", "Rio de Janeiro"),
    "Goiás": (
        "Bahia",
        "Distrito Federal",
        "Mato Grosso",
        "Mato Grosso do Sul",
        "Minas Gerais",
        "Tocantins",
    ),
    "Maranhão": ("Pará", "Piauí", "Tocantins"),
    "Mato Grosso": (
        "Amazonas",
        "Goiás",
        "Mato Grosso do Sul",
        "Pará",
        "Rondônia",
        "Tocantins",
    ),
    "Mato Grosso do Sul": (
        "Goiás",
        "Mato Grosso",
        "Minas Gerais",
        "Paraná",
        "São Paulo",
    ),
    "Minas Gerais": (
        "Bahia",
        "Distrito Federal",
        "Espírito Santo",
        "Goiás",
        "Mato Grosso do Sul",
        "Rio de Janeiro",
        "São Paulo",
    ),
    "Pará": ("Amapá", "Amazonas", "Maranhão", "Mato Grosso", "Roraima", "Tocantins"),
    "Paraíba": ("Ceará", "Pernambuco", "Rio Grande do Norte"),
    "Paraná": ("Mato Grosso do Sul", "Santa Catarina", "São Paulo"),
    "Pernambuco": ("Alagoas", "Bahia", "Ceará", "Paraíba", "Piauí"),
    "Piauí": ("Bahia", "Ceará", "Maranhão", "Tocantins"),
    "Rio de Janeiro": ("Espírito Santo", "Minas Gerais", "São Paulo"),
    "Rio Grande do Norte": ("Ceará", "Paraíba"),
    "Rio Grande do Sul": ("Santa Catarina",),
    "Rondônia": ("Acre", "Amazonas", "Mato Grosso"),
    "Roraima": ("Amazonas", "Pará"),
    "Santa Catarina": ("Paraná", "Rio Grande do Sul"),
    "São Paulo": ("Mato Grosso do Sul", "Minas Gerais", "Paraná", "Rio de Janeiro"),
    "Sergipe": ("Alagoas", "Bahia"),
    "Tocantins": ("Bahia", "Goiás", "Maranhão", "Mato Grosso", "Pará", "Piauí"),
}


# --------------------------------------------------- main

for cidade in brasil.keys():
    buscLarg = criaGrafoNextowrkXComNodes(busca_largura(brasil, cidade))
    print('cidade: ', cidade)
    motraDictPorLinha(busca_largura(brasil, cidade))
    print()
    desenhaGrafo(buscLarg)

for cidade in brasil.keys():
    buscaProf = criaGrafoNextowrkXComNodes(busca_profundidade(brasil, cidade))
    print('Cidade: ', cidade)
    motraDictPorLinha(busca_profundidade(brasil, cidade))
    print()
    desenhaGrafo(buscaProf)




