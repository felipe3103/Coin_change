# 🧩 Dynamic Programming — Coin Change (Checkpoint 2025/2)

> **Curso:** Engenharia de Software  
> **Disciplina:** Dynamic Programming  
> **Professor:** Marcelo Amorim  

---

## 👥 **Integrantes**

| Nome | RM |
|------|------|
| **Felipe Braunstein e Silva** | RM554483 |
| **Felipe do Nascimento Fernandes** | RM554598 |
| **Lorenzo Hayashi Mangini** | RM554901 |

---

## **1. Introdução e Contextualização**

O **problema da troca de moedas (Coin Change Problem)** é um dos desafios mais clássicos da **Programação Dinâmica (PD)**.  
O objetivo é determinar a **menor quantidade de moedas necessárias** para formar um valor monetário **M**, utilizando moedas de valores fixos e quantidade ilimitada.

Esse tipo de problema é um exemplo didático e prático de como **a PD transforma um problema combinatório exponencial** em uma **solução eficiente e sistemática**.

---

## 🎯 **2. Objetivo do Projeto**

Desenvolver e comparar **quatro abordagens distintas** para o problema do troco, explorando desde métodos ingênuos até soluções otimizadas com PD.

O projeto visa:
- Demonstrar a evolução natural de um algoritmo ineficiente até uma versão otimizada.
- Analisar a diferença entre abordagens **recursivas, iterativas e dinâmicas**.
- Ilustrar **conceitos fundamentais de PD**, como *subestrutura ótima* e *subproblemas sobrepostos*.

---

## 🧠 **3. Resumo das Estratégias**

| **Abordagem** | **Tipo** | **Complexidade** | **Observações** |
|----------------|-----------|------------------|------------------|
| **Gulosa** | Iterativa | O(k log k) | Rápida, mas não garante o resultado ótimo em sistemas não canônicos |
| **Recursiva Pura** | Recursiva | Exponencial | Explora todas as possibilidades, extremamente lenta para grandes M |
| **Recursiva com Memoização (Top-Down)** | PD Recursiva | O(M * k) | Armazena subresultados para evitar recomputações |
| **Bottom-Up (Programação Dinâmica)** | PD Iterativa | O(M * k) | Resolve de forma iterativa; ideal para aplicações reais |

> 💡 *“Cada método representa um degrau da evolução algorítmica — do pensamento ingênuo à eficiência sistemática da Programação Dinâmica.”*

---

## 🧩 **4. Lógica do Algoritmo**

### 🔸 **Subestrutura Ótima**
A solução ótima para um valor **M** depende das soluções ótimas dos subproblemas menores.  
A relação de recorrência é dada por:
    `dp[M] = 1 + min(dp[M - c]) # para cada moeda c`
Isso significa que para encontrar a quantidade mínima de moedas que somam M, o algoritmo verifica todos os subvalores `M - c` possíveis, garantindo a escolha da combinação com menor custo.

---
### 🔸 **Subproblemas Sobrepostos**
Durante o processo de cálculo, subvalores como `M - 1`, `M - 3` e `M - 4` são recalculados diversas vezes.  
Ao **armazenar seus resultados** (técnica de memoização), evitamos recomputações e reduzimos o custo total do algoritmo.

Esse princípio é o coração da **Programação Dinâmica**, que substitui esforço repetitivo por **inteligência armazenada**.

---

## 📊 **5. Comparativo de Desempenho**

| **Abordagem** | **Tempo de Execução** | **Espaço Utilizado** | **Garantia de Ótimo** |
|----------------|-----------------------|----------------------|------------------------|
| **Gulosa** | 🔹 Muito rápida | 🔹 Baixo | ❌ Nem sempre |
| **Recursiva Pura** | 🔺 Extremamente lenta | 🔸 Médio | ✅ Sim |
| **Recursiva + Memoização** | ✅ Rápida | 🔹 Baixo | ✅ Sim |
| **Bottom-Up (PD)** | 🟢 Muito rápida | 🔹 Baixo | ✅ Sim |

---

## 🔍 **6. Complexidade Teórica**

| **Função** | **Tempo** | **Espaço** |
|-------------|------------|------------|
| `qtdeMoedas` | O(k log k) | O(1) |
| `qtdeMoedasRec` | O(k^M) | O(M) |
| `qtdeMoedasRecMemo` | O(M * k) | O(M) |
| `qtdeMoedasPD` | O(M * k) | O(M) |

---

## 🧭 **7. Conclusão**

A **Programação Dinâmica** é o ponto de convergência entre **simplicidade** e **eficiência**, permitindo resolver problemas complexos de maneira **determinística e otimizada**.

Ela transforma uma abordagem **exponencial** em uma solução **linear**, aproveitando resultados previamente calculados e reduzindo drasticamente o tempo de execução.

As versões **Top-Down** (com memoização) e **Bottom-Up** (com tabela dinâmica) garantem sempre o **resultado ótimo**, sendo amplamente aplicáveis em contextos como:

- 💰 **Sistemas de troco e otimização financeira**  
- 🚚 **Planejamento logístico e escalonamento de recursos**  
- 🎒 **Problemas de mochila e custo mínimo**

> 💡 *“A eficiência da Programação Dinâmica está em reaproveitar inteligência — cada subproblema resolvido é uma vitória já conquistada.”*
