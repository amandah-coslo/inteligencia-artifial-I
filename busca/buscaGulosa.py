"""
BUSCA GULOSA (GREEDY BEST-FIRST SEARCH)

Baseado no exemplo clássico do livro:
Inteligência Artificial: Uma Abordagem Moderna (Russell & Norvig)

Objetivo:
Encontrar um caminho de Arad até Bucareste.

A Busca Gulosa utiliza:
f(n) = h(n)

Onde:
h(n) = distância em linha reta até Bucareste

Ela NÃO considera o custo já percorrido. Ela apenas escolhe a cidade que aparenta estar mais próxima do destino.

RESULTADO: Arad → Sibiu → Fagaras → Bucharest
"""

from queue import PriorityQueue

# MAPA COMPLETO DA ROMÊNIA (AIMA)
grafo = {
    "Arad": {
        "Zerind": 75,
        "Sibiu": 140,
        "Timisoara": 118
    },

    "Zerind": {
        "Arad": 75,
        "Oradea": 71
    },

    "Oradea": {
        "Zerind": 71,
        "Sibiu": 151
    },

    "Sibiu": {
        "Arad": 140,
        "Oradea": 151,
        "Fagaras": 99,
        "Rimnicu Vilcea": 80
    },

    "Timisoara": {
        "Arad": 118,
        "Lugoj": 111
    },

    "Lugoj": {
        "Timisoara": 111,
        "Mehadia": 70
    },

    "Mehadia": {
        "Lugoj": 70,
        "Drobeta": 75
    },

    "Drobeta": {
        "Mehadia": 75,
        "Craiova": 120
    },

    "Craiova": {
        "Drobeta": 120,
        "Rimnicu Vilcea": 146,
        "Pitesti": 138
    },

    "Rimnicu Vilcea": {
        "Sibiu": 80,
        "Pitesti": 97,
        "Craiova": 146
    },

    "Fagaras": {
        "Sibiu": 99,
        "Bucharest": 211
    },

    "Pitesti": {
        "Rimnicu Vilcea": 97,
        "Craiova": 138,
        "Bucharest": 101
    },

    "Bucharest": {
        "Fagaras": 211,
        "Pitesti": 101,
        "Giurgiu": 90,
        "Urziceni": 85
    },

    "Giurgiu": {
        "Bucharest": 90
    },

    "Urziceni": {
        "Bucharest": 85,
        "Hirsova": 98,
        "Vaslui": 142
    },

    "Hirsova": {
        "Urziceni": 98,
        "Eforie": 86
    },

    "Eforie": {
        "Hirsova": 86
    },

    "Vaslui": {
        "Urziceni": 142,
        "Iasi": 92
    },

    "Iasi": {
        "Vaslui": 92,
        "Neamt": 87
    },

    "Neamt": {
        "Iasi": 87
    }
}

# HEURÍSTICA
# Distância em linha reta até Bucareste.
# Valores retirados do exemplo clássico do livro.
# Quanto menor o valor, mais próxima a cidade parece estar.

heuristica = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Drobeta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374
}


def busca_gulosa(inicio, objetivo):

    # Cria fila de prioridade.
    fila = PriorityQueue()

    # Adiciona Arad na fila.
    # A prioridade é a heurística.
    fila.put(
        (
            heuristica[inicio],
            [inicio]
        )
    )

    # Guarda cidades já visitadas.
    visitados = set()

    while not fila.empty():

        # Remove a cidade com menor heurística.
        _, caminho = fila.get()

        cidade_atual = caminho[-1]

        print(f"\nVisitando: {cidade_atual}")
        print(
            f"Heurística: "
            f"{heuristica[cidade_atual]}"
        )

        # Encontrou Bucareste?
        if cidade_atual == objetivo:

            print("\nObjetivo encontrado!")

            return caminho

        if cidade_atual not in visitados:

            visitados.add(cidade_atual)

            # Analisa cidades vizinhas.
            for vizinho, distancia in grafo[cidade_atual]:

                print(
                    f"  Vizinho: {vizinho}"
                    f" | Distância: {distancia}"
                    f" km"
                    f" | h(n): {heuristica[vizinho]}"
                )

                novo_caminho = caminho + [vizinho]

                # Busca Gulosa usa apenas:
                # f(n) = h(n)
                fila.put(
                    (
                        heuristica[vizinho],
                        novo_caminho
                    )
                )
    return None

resultado = busca_gulosa(
    "Arad",
    "Bucareste"
)

print("\nCaminho encontrado:")
print(" -> ".join(resultado))