# Árvores Binárias de Busca Únicas (Unique BSTs)

## Integrantes do Grupo
- Agos Dalcin
- Antonio Favarin Freire
- Victor Oladio Boehm Lapa

## Descrição do Problema

Este projeto implementa uma solução para o problema de contagem de Árvores Binárias de Busca Únicas (Unique BSTs). O problema consiste em:

> Dado um número n, contar quantas árvores binárias de busca distintas podem ser construídas com n nós numerados de 1 a n.

## Abordagem de Solução

Nossa implementação utiliza **programação dinâmica com memoization**, combinando:
- Recursão para definir a estrutura do problema
- Técnica de memoization (cache) para evitar recálculos desnecessários

### Estratégia

Para resolver este problema:
1. Para cada valor i de 1 até n, consideramos i como a raiz da árvore
2. Os valores de 1 até (i-1) formam a subárvore esquerda
3. Os valores de (i+1) até n formam a subárvore direita
4. O número total de árvores possíveis com raiz i é o produto entre:
   - Número de BSTs possíveis com os elementos à esquerda
   - Número de BSTs possíveis com os elementos à direita
5. Somamos estes valores para todas as possíveis raízes

### Implementação

- Utilizamos um dicionário Python (`dict`) como hashtable para implementar o cache
- A função verifica primeiro se o resultado já existe no cache antes de calcular
- Os resultados são armazenados no cache para uso futuro
- Acesso aos valores em tempo O(1), conforme requisito do problema

## Como Executar

```bash
python main.py
```

## Complexidade

- **Tempo**: O(n²) com memoization (em vez de O(2^n) sem otimização)
- **Espaço**: O(n) para armazenar o cache

## Exemplo de Saída

```
Número de BSTs únicos para diferentes valores de n:
n = 1: 1
n = 2: 2
n = 3: 5
n = 4: 14
n = 5: 42
n = 6: 132
n = 7: 429
n = 8: 1430
n = 9: 4862
n = 10: 16796
```

## Observação Matemática

Os resultados obtidos correspondem aos Números de Catalan, uma importante sequência matemática em combinatória.
