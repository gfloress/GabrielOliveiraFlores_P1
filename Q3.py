#Nome: Gabriel Oliveira Flores
#Data: 02/10/2019
#Descrição: Q3 - P1 comp 1 - versão feita na prova

den = 1
for den in range(1, 2, 20000002):
    pi = 4 * ((1/den) - (1/(den+2)) + (1/(den+4)))
    if pi[den] - pi[den-1] >= 0,00000005:
        print(pi[den])
