# 🔍 Busca Gulosa (Greedy Search) e Busca A* (A-Star)

<div align="center">

![AI Search](https://img.shields.io/badge/IA-Algoritmos%20de%20Busca-blue)
![Python](https://img.shields.io/badge/Python-Exemplos-green)
![Status](https://img.shields.io/badge/Status-Educacional-success)

</div>

## 📖 Introdução

Algoritmos de busca são fundamentais em Inteligência Artificial, robótica, sistemas de navegação e resolução de problemas.

Dois dos algoritmos mais conhecidos são:

- **Busca Gulosa (Greedy Best-First Search)**
- **Busca A\* (A-Star Search)**

Embora ambos utilizem uma **heurística** para encontrar caminhos, eles possuem comportamentos e garantias diferentes.

---

# 🟢 Busca Gulosa (Greedy Search)

## Conceito

A Busca Gulosa escolhe sempre o nó que **parece estar mais próximo do objetivo**, considerando apenas uma estimativa heurística.

Sua função de avaliação é:

:contentReference[oaicite:0]{index=0}

Onde:

- **f(n)** = valor usado para escolher o próximo nó
- **h(n)** = estimativa da distância até o objetivo

---

## Como funciona

1. Avalia todos os nós disponíveis.
2. Escolhe aquele com menor valor heurístico.
3. Ignora o custo já percorrido.
4. Repete até encontrar o objetivo.

---

## Exemplo

Imagine o seguinte cenário:

```text
A ---- B ---- G
 \     
  \    
   C
```

Heurísticas:

| Nó | h(n) |
|-----|------|
| A | 10 |
| B | 2 |
| C | 1 |
| G | 0 |

A Busca Gulosa escolherá:

```text
A → C
```

porque **C possui menor heurística**, mesmo que não seja o melhor caminho.

---

## Vantagens

✅ Simples de implementar

✅ Geralmente rápida

✅ Boa quando se deseja uma solução rapidamente

---

## Desvantagens

❌ Pode encontrar caminhos ruins

❌ Não garante a melhor solução

❌ Pode ficar presa em escolhas aparentemente boas

---

# ⭐ Busca A* (A-Star)

## Conceito

A Busca A* combina:

- custo já percorrido
- estimativa até o objetivo

Sua função é:

:contentReference[oaicite:1]{index=1}

Onde:

| Símbolo | Significado |
|----------|-------------|
| g(n) | custo do início até o nó atual |
| h(n) | estimativa até o objetivo |
| f(n) | custo total estimado |

---

## Como funciona

O algoritmo avalia:

```text
Custo já gasto
+
Estimativa restante
```

e escolhe o nó com menor valor total.

---

## Exemplo

```text
A ---- B ---- G
 \     
  \    
   C
```

Custos:

```text
A → B = 2
B → G = 2

A → C = 1
C → G = 10
```

Heurísticas:

```text
h(B)=2
h(C)=1
```

Cálculo:

| Nó | g(n) | h(n) | f(n) |
|-----|------|------|------|
| B | 2 | 2 | 4 |
| C | 1 | 1 | 2 |

Inicialmente A* explora C.

Depois percebe que:

```text
A → C → G = 11
```

enquanto

```text
A → B → G = 4
```

e encontra o melhor caminho.

---

## Vantagens

✅ Completo

✅ Ótimo (encontra o melhor caminho)

✅ Muito utilizado em jogos e GPS

✅ Considerado um dos melhores algoritmos de busca heurística

---

## Desvantagens

❌ Consome mais memória

❌ Pode ser lento em grafos gigantes

❌ Depende da qualidade da heurística

---

# ⚖️ Comparação

| Característica | Busca Gulosa | Busca A* |
|----------------|--------------|----------|
| Usa heurística | ✅ | ✅ |
| Considera custo percorrido | ❌ | ✅ |
| Encontra solução rapidamente | ✅ | ⚠️ |
| Garante melhor caminho | ❌ | ✅ |
| Consumo de memória | Baixo | Maior |
| Uso em GPS | ❌ | ✅ |
| Uso em Jogos | ⚠️ | ✅ |

---

# 🎯 Resumo Visual

```text
BUSCA GULOSA

Escolha:
↓
Menor h(n)

Objetivo:
↓
Chegar rápido

Qualidade:
↓
Nem sempre ótima
```

```text
BUSCA A*

Escolha:
↓
Menor g(n)+h(n)

Objetivo:
↓
Melhor caminho

Qualidade:
↓
Ótima (quando a heurística é admissível)
```

---

# 🌍 Aplicações Reais

### Busca Gulosa

- Sistemas simples de navegação
- Problemas de otimização rápida
- IA básica

### Busca A*

- Google Maps
- Waze
- Robótica
- Planejamento de rotas
- NPCs em jogos
- Sistemas autônomos

---

# 💻 Exemplo Simplificado em Python

## Busca Gulosa

```python
f = h(n)
```

Escolhe apenas o nó mais próximo do objetivo.

---

## Busca A*

```python
f = g(n) + h(n)
```

Considera:

- caminho já percorrido
- caminho restante estimado

---

# 📚 Conclusão

A principal diferença entre os algoritmos está na forma como eles avaliam os caminhos:

- **Busca Gulosa** → considera apenas a estimativa até o objetivo.
- **Busca A\*** → considera o custo já percorrido e a estimativa restante.

Por isso:

> A Busca Gulosa é mais rápida, porém pode tomar decisões ruins.

> A Busca A* costuma ser mais eficiente para encontrar o melhor caminho possível.

---

## 👨‍💻 Autor

Projeto desenvolvido para estudos de **Inteligência Artificial e Algoritmos de Busca**.

⭐ Se este conteúdo ajudou você, considere deixar uma estrela no repositório.
