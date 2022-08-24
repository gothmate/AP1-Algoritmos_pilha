AP1 de Algoritmos e Estrutura de Dados (UNIGRANRIO - 2022-2)

Escrever um programa que leia 30 números e que, para cada número lido, verifique
e codifique de acordo com as regras abaixo:
    a. Se o número for par, empilhe em uma lista chamada PAR;
    b. Se o número for ímpar, empilhe em uma lista chamada IMPAR;
    c. Se for zero, desempilhe um elemento de cada pilha. Caso a pilha esteja vazia,
exiba na tela uma mensagem informando que a lista está vazia.
    d. Ao final do programa, desempilhe todos os elementos das duas listas exibindo-os
na tela.


CONSOLE RESULT:
=======================================================================================

Digite o 1º número: 1
Insere valor 1 no topo da pilha ÍMPARES: [1 -> None]
Digite o 2º número: 2
Insere valor 2 no topo da pilha PARES: [2 -> None]
Digite o 3º número: 3
Insere valor 3 no topo da pilha ÍMPARES: [3 -> 1 -> None]
Digite o 4º número: 4
Insere valor 4 no topo da pilha PARES: [4 -> 2 -> None]
Digite o 5º número: 5
Insere valor 5 no topo da pilha ÍMPARES: [5 -> 3 -> 1 -> None]
Digite o 6º número: 6
Insere valor 6 no topo da pilha PARES: [6 -> 4 -> 2 -> None]
Digite o 7º número: 7
Insere valor 7 no topo da pilha ÍMPARES: [7 -> 5 -> 3 -> 1 -> None]
Digite o 8º número: 8
Insere valor 8 no topo da pilha PARES: [8 -> 6 -> 4 -> 2 -> None]
Digite o 9º número: 9
Insere valor 9 no topo da pilha ÍMPARES: [9 -> 7 -> 5 -> 3 -> 1 -> None]
Digite o 10º número: 10
Insere valor 10 no topo da pilha PARES: [10 -> 8 -> 6 -> 4 -> 2 -> None]
Digite o 11º número: 11
Insere valor 11 no topo da pilha ÍMPARES: [11 -> 9 -> 7 -> 5 -> 3 -> 1 -> None]
Digite o 12º número: 12
Insere valor 12 no topo da pilha PARES: [12 -> 10 -> 8 -> 6 -> 4 -> 2 -> None]
Digite o 13º número: 13
Insere valor 13 no topo da pilha ÍMPARES: [13 -> 11 -> 9 -> 7 -> 5 -> 3 -> 1 -> None]
Digite o 14º número: 14
Insere valor 14 no topo da pilha PARES: [14 -> 12 -> 10 -> 8 -> 6 -> 4 -> 2 -> None]
Digite o 15º número: 0
Digite o 16º número: 0
Digite o 17º número: 16
Insere valor 16 no topo da pilha PARES: [16 -> 10 -> 8 -> 6 -> 4 -> 2 -> None]
Digite o 18º número: 15
Insere valor 15 no topo da pilha ÍMPARES: [15 -> 9 -> 7 -> 5 -> 3 -> 1 -> None]
Digite o 19º número: 17
Insere valor 17 no topo da pilha ÍMPARES: [17 -> 15 -> 9 -> 7 -> 5 -> 3 -> 1 -> None]
Digite o 20º número: 18
Insere valor 18 no topo da pilha PARES: [18 -> 16 -> 10 -> 8 -> 6 -> 4 -> 2 -> None]
Digite o 21º número: 19
Insere valor 19 no topo da pilha ÍMPARES: [19 -> 17 -> 15 -> 9 -> 7 -> 5 -> 3 -> 1 -> None]
Digite o 22º número: 0
Digite o 23º número: 20
Insere valor 20 no topo da pilha PARES: [20 -> 16 -> 10 -> 8 -> 6 -> 4 -> 2 -> None]
Digite o 24º número: 21
Insere valor 21 no topo da pilha ÍMPARES: [21 -> 17 -> 15 -> 9 -> 7 -> 5 -> 3 -> 1 -> None]
Digite o 25º número: 22
Insere valor 22 no topo da pilha PARES: [22 -> 20 -> 16 -> 10 -> 8 -> 6 -> 4 -> 2 -> None]
Digite o 26º número: 23
Insere valor 23 no topo da pilha ÍMPARES: [23 -> 21 -> 17 -> 15 -> 9 -> 7 -> 5 -> 3 -> 1 -> None]
Digite o 27º número: 24
Insere valor 24 no topo da pilha PARES: [24 -> 22 -> 20 -> 16 -> 10 -> 8 -> 6 -> 4 -> 2 -> None]
Digite o 28º número: 25
Insere valor 25 no topo da pilha ÍMPARES: [25 -> 23 -> 21 -> 17 -> 15 -> 9 -> 7 -> 5 -> 3 -> 1 -> None]
Digite o 29º número: 0
Digite o 30º número: 0
Visualizando a Pilha PARES completa:  [20 -> 16 -> 10 -> 8 -> 6 -> 4 -> 2 -> None]
Removendo elemento que está no topo da pilha PARES:  [16 -> 10 -> 8 -> 6 -> 4 -> 2 -> None]
Removendo elemento que está no topo da pilha PARES:  [10 -> 8 -> 6 -> 4 -> 2 -> None]
Removendo elemento que está no topo da pilha PARES:  [8 -> 6 -> 4 -> 2 -> None]
Removendo elemento que está no topo da pilha PARES:  [6 -> 4 -> 2 -> None]
Removendo elemento que está no topo da pilha PARES:  [4 -> 2 -> None]
Removendo elemento que está no topo da pilha PARES:  [2 -> None]
Removendo elemento que está no topo da pilha PARES:  [None]
Visualizando a Pilha ÍMPARES completa:  [21 -> 17 -> 15 -> 9 -> 7 -> 5 -> 3 -> 1 -> None]
Removendo elemento que está no topo da pilha ÍMPARES:  [17 -> 15 -> 9 -> 7 -> 5 -> 3 -> 1 -> None]  
Removendo elemento que está no topo da pilha ÍMPARES:  [15 -> 9 -> 7 -> 5 -> 3 -> 1 -> None]        
Removendo elemento que está no topo da pilha ÍMPARES:  [9 -> 7 -> 5 -> 3 -> 1 -> None]
Removendo elemento que está no topo da pilha ÍMPARES:  [7 -> 5 -> 3 -> 1 -> None]
Removendo elemento que está no topo da pilha ÍMPARES:  [5 -> 3 -> 1 -> None]
Removendo elemento que está no topo da pilha ÍMPARES:  [3 -> 1 -> None]
Removendo elemento que está no topo da pilha ÍMPARES:  [1 -> None]
Removendo elemento que está no topo da pilha ÍMPARES:  [None]
PS C:\Users\gothm\Documents\UNIGRANRIO\4º período\Algoritmos e Estrutura de Dados\AP1> git add .
PS C:\Users\gothm\Documents\UNIGRANRIO\4º período\Algoritmos e Estrutura de Dados\AP1> python3 .\ap1_comClasses.py                                                                                      Digite o 1º número: 3
Insere valor 3 no topo da pilha ÍMPARES: [3 -> None]
Digite o 2º número: 5
Insere valor 5 no topo da pilha ÍMPARES: [5 -> 3 -> None]
Digite o 3º número: 1
Insere valor 1 no topo da pilha ÍMPARES: [1 -> 5 -> 3 -> None]
Digite o 4º número: 2
Insere valor 2 no topo da pilha PARES: [2 -> None]
Digite o 5º número: 4
Insere valor 4 no topo da pilha PARES: [4 -> 2 -> None]
Digite o 6º número: 6
Insere valor 6 no topo da pilha PARES: [6 -> 4 -> 2 -> None]
Digite o 7º número: a
Somente números são permitidos. invalid literal for int() with base 10: 'a'
Digite o 8º número: 12
Insere valor 12 no topo da pilha PARES: [12 -> 6 -> 4 -> 2 -> None]
Digite o 9º número: 0
Digite o 10º número: 6
Insere valor 6 no topo da pilha PARES: [6 -> 6 -> 4 -> 2 -> None]
Digite o 11º número: 7
Insere valor 7 no topo da pilha ÍMPARES: [7 -> 5 -> 3 -> None]
Digite o 12º número: 71
Insere valor 71 no topo da pilha ÍMPARES: [71 -> 7 -> 5 -> 3 -> None]
Digite o 13º número: 73
Insere valor 73 no topo da pilha ÍMPARES: [73 -> 71 -> 7 -> 5 -> 3 -> None]
Digite o 14º número: 31
Insere valor 31 no topo da pilha ÍMPARES: [31 -> 73 -> 71 -> 7 -> 5 -> 3 -> None]
Digite o 15º número: 32
Insere valor 32 no topo da pilha PARES: [32 -> 6 -> 6 -> 4 -> 2 -> None]
Digite o 16º número: 22
Insere valor 22 no topo da pilha PARES: [22 -> 32 -> 6 -> 6 -> 4 -> 2 -> None]
Digite o 17º número: 10
Insere valor 10 no topo da pilha PARES: [10 -> 22 -> 32 -> 6 -> 6 -> 4 -> 2 -> None]
Digite o 18º número: 90
Insere valor 90 no topo da pilha PARES: [90 -> 10 -> 22 -> 32 -> 6 -> 6 -> 4 -> 2 -> None]
Digite o 19º número: 187
Insere valor 187 no topo da pilha ÍMPARES: [187 -> 31 -> 73 -> 71 -> 7 -> 5 -> 3 -> None]
Digite o 20º número: 964
Insere valor 964 no topo da pilha PARES: [964 -> 90 -> 10 -> 22 -> 32 -> 6 -> 6 -> 4 -> 2 -> None]
Digite o 21º número: 100
Insere valor 100 no topo da pilha PARES: [100 -> 964 -> 90 -> 10 -> 22 -> 32 -> 6 -> 6 -> 4 -> 2 -> None]
Digite o 22º número: 0
Digite o 23º número: 0
Digite o 24º número: 13
Insere valor 13 no topo da pilha ÍMPARES: [13 -> 73 -> 71 -> 7 -> 5 -> 3 -> None]
Digite o 25º número: 19
Insere valor 19 no topo da pilha ÍMPARES: [19 -> 13 -> 73 -> 71 -> 7 -> 5 -> 3 -> None]
Digite o 26º número: 2
Insere valor 2 no topo da pilha PARES: [2 -> 90 -> 10 -> 22 -> 32 -> 6 -> 6 -> 4 -> 2 -> None]
Digite o 27º número: 111
Insere valor 111 no topo da pilha ÍMPARES: [111 -> 19 -> 13 -> 73 -> 71 -> 7 -> 5 -> 3 -> None]
Digite o 28º número: -32
Insere valor -32 no topo da pilha PARES: [-32 -> 2 -> 90 -> 10 -> 22 -> 32 -> 6 -> 6 -> 4 -> 2 -> None]
Digite o 29º número: -17
Insere valor -17 no topo da pilha ÍMPARES: [-17 -> 111 -> 19 -> 13 -> 73 -> 71 -> 7 -> 5 -> 3 -> None]
Digite o 30º número: 95
Insere valor 95 no topo da pilha ÍMPARES: [95 -> -17 -> 111 -> 19 -> 13 -> 73 -> 71 -> 7 -> 5 -> 3 -> None]
Visualizando a Pilha PARES completa:  [-32 -> 2 -> 90 -> 10 -> 22 -> 32 -> 6 -> 6 -> 4 -> 2 -> None]
Removendo elemento que está no topo da pilha PARES:  [2 -> 90 -> 10 -> 22 -> 32 -> 6 -> 6 -> 4 -> 2 -> None]
Removendo elemento que está no topo da pilha PARES:  [90 -> 10 -> 22 -> 32 -> 6 -> 6 -> 4 -> 2 -> None]
Removendo elemento que está no topo da pilha PARES:  [10 -> 22 -> 32 -> 6 -> 6 -> 4 -> 2 -> None]   
Removendo elemento que está no topo da pilha PARES:  [22 -> 32 -> 6 -> 6 -> 4 -> 2 -> None]
Removendo elemento que está no topo da pilha PARES:  [32 -> 6 -> 6 -> 4 -> 2 -> None]
Removendo elemento que está no topo da pilha PARES:  [6 -> 6 -> 4 -> 2 -> None]
Removendo elemento que está no topo da pilha PARES:  [6 -> 4 -> 2 -> None]
Removendo elemento que está no topo da pilha PARES:  [4 -> 2 -> None]
Removendo elemento que está no topo da pilha PARES:  [2 -> None]
Removendo elemento que está no topo da pilha PARES:  [None]
Visualizando a Pilha ÍMPARES completa:  [95 -> -17 -> 111 -> 19 -> 13 -> 73 -> 71 -> 7 -> 5 -> 3 -> None]
Removendo elemento que está no topo da pilha ÍMPARES:  [111 -> 19 -> 13 -> 73 -> 71 -> 7 -> 5 -> 3 -> None]
Removendo elemento que está no topo da pilha ÍMPARES:  [19 -> 13 -> 73 -> 71 -> 7 -> 5 -> 3 -> None]Removendo elemento que está no topo da pilha ÍMPARES:  [13 -> 73 -> 71 -> 7 -> 5 -> 3 -> None]      
Removendo elemento que está no topo da pilha ÍMPARES:  [73 -> 71 -> 7 -> 5 -> 3 -> None]Removendo elemento que está no topo da pilha ÍMPARES:  [71 -> 7 -> 5 -> 3 -> None]
Removendo elemento que está no topo da pilha ÍMPARES:  [7 -> 5 -> 3 -> None]
Removendo elemento que está no topo da pilha ÍMPARES:  [5 -> 3 -> None]
Removendo elemento que está no topo da pilha ÍMPARES:  [3 -> None]
Removendo elemento que está no topo da pilha ÍMPARES:  [None]