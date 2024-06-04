import random

linha = int(input("Digite o número de linhas: "))
coluna = int(input("Digite o número de colunas: "))

def matrizes(linha,coluna):
    matriz=[]
    for i in range(linha):
        linhas=[]
        for j in range(coluna):
            elementos=random.randint(1, 20)
            linhas.append(elementos)
        matriz.append(linhas)
    return matriz

m=matrizes(linha,coluna)

def printMatrizes(matriz):
    for linha in matriz:
        print(linha)

printMatrizes(m)

def parMatriz(linha,coluna,matriz):
    p = 0
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] % 2 == 0:
                p += matriz[i][j]
    return (f"A soma dos numeros pares dentro da matriz é: {p}")

parMatriz(linha,coluna,m)

escolhaColuna = int(input("Digite a coluna que desejas somar: "))

def soma_coluna(matriz, escolhaColuna):
    if (escolhaColuna - 1) < 0 or (escolhaColuna - 1) >= len(matriz[0]):
        return (f"A coluna {escolhaColuna} não existe na matriz.")
    
    somaColuna = 0
    for i in range(len(matriz)):
        somaColuna += matriz[i][escolhaColuna - 1]
    
    return (f"A soma dos elementos da coluna {escolhaColuna} é: {somaColuna}")

soma=soma_coluna(m,escolhaColuna)
print(soma)

escolherLinha = int(input("Digite a linha que deseja achar o maior valor: "))

def maior_valor_linha(matriz, escolherLinha):
    if (escolherLinha - 1) < 0 or (escolherLinha - 1) >= len(matriz):
        return (f"A linha {escolherLinha} não existe na matriz.")
    
    valor_max =  matriz[escolherLinha - 1][0]
    for valor in matriz[escolherLinha - 1]:
        if valor > valor_max:
            valor_max = valor

    return (f"O maior valor da linha {escolherLinha} é: {valor_max}")
maiorValor = maior_valor_linha(m,escolherLinha)

print(maiorValor)

def matrizEspecifica():
    matriz3 = []
    for i in range(10):
        linha3 = []
        for j in range(10):
            if i < j:
                valor = 2 * i + 7 * j + 2
            elif i == j:
                valor = 3 * i ** 2 + 1
            else:
                valor = 4 * i * 3 + 5 * j * 2 + 1
            linha3.append(valor)
        matriz3.append(linha3)
    return matriz3

MatrizEspecifica = matrizEspecifica()
printMatrizes(matrizEspecifica())

