"""
BUSCA A* (A-STAR)

Baseado no exemplo clássico da Romênia presente no livro de Russell e Norvig.

Objetivo:
Encontrar o melhor caminho entre Arad e Bucareste. 

A* utiliza: 
f(n) = g(n) + h(n)

Onde:
g(n) = custo real já percorrido
h(n) = distância estimada até Bucareste
f(n) = custo total estimado

Diferente da Busca Gulosa, A* considera tanto o passado quanto o futuro.

RESULTADO: Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest
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

def busca_a_estrela(inicio, objetivo):

    # Fila de prioridade.
    fila = PriorityQueue()

    # Adiciona cidade inicial.
    fila.put(
        (
            0,
            inicio,
            [inicio]
        )
    )

    # Guarda os custos acumulados.
    custos = {
        inicio: 0
    }

    while not fila.empty():
        _, cidade_atual, caminho = fila.get()

        print(f"\nVisitando: {cidade_atual}")

        if cidade_atual == objetivo:
            print("\nObjetivo encontrado!")
            return caminho

        # Analisa cada cidade vizinha.
        for vizinho, distancia in grafo[cidade_atual]:

            # g(n)
            # Quanto já gastamos para chegar até o vizinho.
            novo_custo = (
                custos[cidade_atual]
                + distancia
            )

            # h(n)
            # Distância estimada até Bucareste.
            h = heuristica[vizinho]

            # f(n)
            # Fórmula do A*
            f = novo_custo + h

            print(
                f"  Vizinho: {vizinho}"
            )

            print(
                f"    g(n): {novo_custo}"
            )

            print(
                f"    h(n): {h}"
            )

            print(
                f"    f(n): {f}"
            )

            if (
                vizinho not in custos
                or
                novo_custo < custos[vizinho]
            ):

                custos[vizinho] = novo_custo

                fila.put(
                    (
                        f,
                        vizinho,
                        caminho + [vizinho]
                    )
                )

    return None

resultado = busca_a_estrela(
    "Arad",
    "Bucareste"
)

print("\nMelhor caminho encontrado:")
print(" -> ".join(resultado))