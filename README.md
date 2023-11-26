# Problema de Transporte - README

## Integrantes 
- Nome: Flaviano Cássio da Cruz Matozinhos
- Matricula: E00784

- Nome: Eder Lucas de Almeida Oliveira
- Matricula: E01814

## Contextualização do Problema

O Problema de Transporte é um clássico problema de otimização que envolve o transporte de mercadorias de vários fornecedores para vários destinos, minimizando (ou maximizando) o custo total. No contexto deste problema, temos um número fixo de fornecedores, destinos, ofertas de fornecedores e demandas de destinos.

## Modelagem Matemática

### Dados do Problema

- Oferta de Fornecedores: [100, 150, 200]
- Demanda de Destinos: [120, 80, 170]
- Matriz de Custo de Transporte:
- [[4, 6, 8],
  [3, 5, 7],
  [2, 4, 6]]

  
### Variáveis de Decisão

- \(x_{i,j}\): Quantidade a ser transportada do fornecedor \(i\) para o destino \(j\).

### Objetivo

Minimizar (ou maximizar) o custo total de transporte, representado pela soma dos produtos da quantidade transportada pelo custo de transporte correspondente.

### Restrições

1. Restrições de Oferta: A quantidade total fornecida por cada fornecedor não deve exceder sua capacidade de oferta.
2. Restrições de Demanda: A quantidade total demandada por cada destino deve ser atendida.

## Exemplo de Solução

Considerando os dados fornecidos, o algoritmo de programação linear foi utilizado para encontrar uma solução ótima. O resultado foi:

### Matriz de Transporte

[[0.0, 0.0, 100.0],
[120.0, 30.0, 0.0],
[0.0, 50.0, 70.0]]


### Custo Máximo

O custo máximo associado a esta solução é 1930.

## Interpretação dos Resultados

A matriz de transporte indica a quantidade a ser transportada de cada fornecedor para cada destino. O custo máximo representa o custo total associado a essa distribuição. Neste exemplo, a solução sugere uma matriz de transporte que maximiza o custo total, dadas as restrições de oferta e demanda.

## Implementação do Algoritmo

O código completo em Python para resolver o Problema de Transporte pode ser encontrado em [trabalhoPo.py](trabalhoPo.py).

## Arquivos Necessários

- [trabalhoPo.py](trabalhoPo.py): Código Python para resolver o Problema de Transporte.
- [README.md](README.md): Este arquivo de documentação.


