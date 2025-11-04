"""
Coin Change - Dynamic Programming Checkpoint (2025/2)
-----------------------------------------------------
Implementação de quatro abordagens para o problema da menor quantidade de moedas
que somam exatamente o montante M, com moedas de disponibilidade ilimitada.

Funções expostas:
    - qtdeMoedas(M, moedas):      Estratégia gulosa (iterativa) — NÃO garante ótimo em bases gerais.
    - qtdeMoedasRec(M, moedas):   Recursiva pura (sem memoização).
    - qtdeMoedasRecMemo(M, moedas): Recursiva com memoização (Top-Down).
    - qtdeMoedasPD(M, moedas):    Programação Dinâmica Bottom-Up.


**Integrantes**
Felipe Braunstein e Silva | RM554483
Felipe do Nascimento Fernandes | RM554598
Lorenzo Hayashi Mangini | RM554901
"""

from functools import lru_cache
from math import inf
from typing import List

def _validar_entrada(M: int, moedas: List[int]) -> None:
    if not isinstance(M, int) or M < 0:
        raise ValueError("M deve ser um inteiro >= 0.")
    if not moedas or any((not isinstance(c, int) or c <= 0) for c in moedas):
        raise ValueError("moedas deve ser uma lista de inteiros positivos.")

def qtdeMoedas(M: int, moedas: List[int]) -> int:
    """
    Calcula a quantidade de moedas via estratégia gulosa (iterativa), escolhendo
    sempre a maior moeda possível a cada passo. NÃO garante solução ótima para
    todos os conjuntos de moedas (não-canônicos).

    Parâmetros:
        M (int): montante alvo (>= 0).
        moedas (List[int]): valores de moedas disponíveis (ilimitadas), inteiros positivos.

    Retorno:
        int: menor quantidade encontrada pela estratégia gulosa se formar exatamente M;
             -1 se não for possível formar M com a estratégia gulosa.

    Complexidade (teórica):
        - Tempo:
            O(k log k) para ordenar as moedas em ordem decrescente + O(k) para uma passada
            usando divisão inteira (sem repetidas subtrações), logo O(k log k).
            Onde k = número de tipos de moedas.
          Ω(k) e Θ(k log k) considerando a ordenação como parte do algoritmo.
        - Espaço: O(1) além da lista de entrada (desconsiderando custo da ordenação in-place).
    """
    _validar_entrada(M, moedas)
    if M == 0:
        return 0
    moedas_sorted = sorted(moedas, reverse=True)
    restante = M
    total = 0
    for c in moedas_sorted:
        if c <= restante:
            q = restante // c
            total += q
            restante -= q * c
        if restante == 0:
            return total
    return -1

def qtdeMoedasRec(M: int, moedas: List[int]) -> int:
    """
    Calcula a menor quantidade de moedas por recursão pura (ingênua), explorando
    todas as possibilidades sem cache/memoização.

    Parâmetros:
        M (int): montante alvo (>= 0).
        moedas (List[int]): valores de moedas disponíveis (ilimitadas), inteiros positivos.

    Retorno:
        int: menor quantidade de moedas para somar M; -1 se impossível.

    Complexidade (teórica):
        - Tempo: Exponencial no pior caso. Uma limitação superior grosseira é O(k^M)
          (cada nível tenta até k escolhas), embora na prática haja poda quando M < 0.
          Em termos assintóticos, é inaceitável para M grande.
          Ω(1) para casos triviais, Θ(exponencial).
        - Espaço: O(M) devido à profundidade máxima da recursão.
    """
    _validar_entrada(M, moedas)

    def rec(x: int) -> int:
        if x == 0:
            return 0
        if x < 0:
            return inf
        melhor = inf
        for c in moedas:
            res = rec(x - c)
            if res != inf:
                melhor = min(melhor, 1 + res)
        return melhor

    ans = rec(M)
    return -1 if ans == inf else ans

def qtdeMoedasRecMemo(M: int, moedas: List[int]) -> int:
    """
    Calcula a menor quantidade de moedas por recursão com memoização (Top-Down).
    Usa cache para evitar recomputar subproblemas.

    Parâmetros:
        M (int): montante alvo (>= 0).
        moedas (List[int]): valores de moedas disponíveis (ilimitadas), inteiros positivos.

    Retorno:
        int: menor quantidade de moedas; -1 se impossível.

    Complexidade (teórica):
        - Tempo: O(M * k), pois cada submontante 0..M é resolvido no máx. uma vez,
          e para cada um testamos k moedas.
          Ω(M) e Θ(M * k).
        - Espaço: O(M) para cache + O(M) de pilha no pior caso (profundidade).
    """
    _validar_entrada(M, moedas)

    @lru_cache(maxsize=None)
    def solve(x: int) -> int:
        if x == 0:
            return 0
        if x < 0:
            return inf
        best = inf
        for c in moedas:
            res = solve(x - c)
            if res != inf:
                best = min(best, 1 + res)
        return best

    ans = solve(M)
    return -1 if ans == inf else ans

def qtdeMoedasPD(M: int, moedas: List[int]) -> int:
    """
    Calcula a menor quantidade de moedas com Programação Dinâmica Bottom-Up.
    Define dp[i] como o mínimo de moedas para somar exatamente i. Inicializa dp[0]=0
    e dp[i]=inf para i>0. Para cada i de 1..M, atualiza dp[i] = min(dp[i], 1+dp[i-c])
    para cada moeda c <= i.

    Parâmetros:
        M (int): montante alvo (>= 0).
        moedas (List[int]): valores de moedas disponíveis (ilimitadas), inteiros positivos.

    Retorno:
        int: menor quantidade de moedas; -1 se impossível.

    Complexidade (teórica):
        - Tempo: O(M * k) (duplo laço: M estados x k moedas).
          Ω(M) e Θ(M * k).
        - Espaço: O(M).
    """
    _validar_entrada(M, moedas)
    dp = [inf] * (M + 1)
    dp[0] = 0
    for i in range(1, M + 1):
        for c in moedas:
            if c <= i and dp[i - c] != inf:
                dp[i] = min(dp[i], 1 + dp[i - c])
    return -1 if dp[M] == inf else dp[M]

if __name__ == "__main__":
    exemplos = [
        (6, [1,3,4]),   # guloso falha (ótimo=2, guloso=3)
        (11, [1,5,7]),  # vários caminhos
        (23, [2,4,6]),  # impossível (ímpar com apenas pares)
        (0, [1,2,5])    # base
    ]
    funs = [qtdeMoedas, qtdeMoedasRec, qtdeMoedasRecMemo, qtdeMoedasPD]
    for M, moedas in exemplos:
        print(f"\nM={M}, moedas={moedas}")
        for f in funs:
            try:
                print(f"  {f.__name__}: {f(M, moedas)}")
            except Exception as e:
                print(f"  {f.__name__}: ERRO -> {e}")
