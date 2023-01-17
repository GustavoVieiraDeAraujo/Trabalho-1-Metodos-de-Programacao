"""
Funções que implementam a verificação do caso das 8 rainhas.
"""

def posiciona_rainhas_no_tabuleiro(entrada):
    '''
    Esta função recebe uma entrada ( string com uma sequencia de zeros
    e uns separados a cada 8 algorismo por um espaço ).A patir dessa
    entrada a função monta uma matriz que representa essa entradae retorna
    ela.
    '''
    tabuleiro = []
    for linha in entrada.split():
        tabuleiro.append([int(elemento) for elemento in linha])
    return tabuleiro

def pega_as_posicoes_das_rainhas(tabuleiro):
    '''
    Esta função recebe uma matriz que representa um tabuleiro de xadrez.
    A função percorre essa matriz salvando a posição das rainhas, as quais
    são representadas pelo algorismo 1, e retorna uma lista com as posições.
    '''
    lista_das_posicoes = []
    for i in range(8):
        for j in range(8):
            if tabuleiro[i][j] == 1:
                lista_das_posicoes.append([i, j])
    return lista_das_posicoes

def verifica_se_o_tabuleiro_tem_8_rainhas(tabuleiro):
    '''
    Esta função recebe uma matriz que representa um tabuleiro de xadrez.
    A função percorre essa matriz contando a quantidade de rainhas presentes
    no tabuleiro, as quais são representadas pelo algorismo 1, e retorna True
    se tiver 8 rainhas e False se tiver mais ou menos que 8 rainhas.
    '''
    contador = 0
    for linha in tabuleiro:
        for posicao in linha:
            if posicao == 1:
                contador += 1
    if contador == 8:
        return True
    return False

def verifica_se_o_tabalueiro_tem_64_posicoes(tabuleiro):
    '''
    Esta função recebe uma matriz que representa um tabuleiro de xadrez.
    Primeiro a função verifica se o tabuleiro tem 8 linhas, após isso ela
    verifica se cada linha tem 8 elementos.Caso o tabuleiro não tenha 8
    linha ou 8 elementos em todas as linhas ela retorna false, caso contrario
    ela retorna true.
    '''
    if len(tabuleiro) == 8:
        for linha in tabuleiro:
            if len(linha) != 8:
                return False
        return True
    return False

def verifica_as_diagonais_da_rainha(tabuleiro, posicao):
    '''
    Esta função recebe uma matriz que representa um tabuleiro de xadrez,
    bem como a posição de uma rainha.Em seguida a função verifica se existe
    outras rainhas na diagonais da posição dessa rainha, caso exista uma rainha
    em alguma diagonal a função retorna False, caso contrario retorna True.
    '''
    linha = posicao[0]
    coluna = posicao[1]

    # superior esquerda
    while(linha != 0 and coluna != 0):
        linha -= 1
        coluna -= 1
        if tabuleiro[linha][coluna] == 1:
            return False

    linha = posicao[0]
    coluna = posicao[1]

    # superior direita
    while(linha !=0 and coluna != 7):
        linha -= 1
        coluna += 1
        if tabuleiro[linha][coluna] == 1:
            return False

    linha = posicao[0]
    coluna = posicao[1]

    # inferior esquerda
    while(linha != 7 and coluna != 0):
        linha += 1
        coluna -= 1
        if tabuleiro[linha][coluna] == 1:
            return False

    linha = posicao[0]
    coluna = posicao[1]

    # inferior direita
    while(linha != 7 and coluna != 7):
        linha += 1
        coluna += 1
        if tabuleiro[linha][coluna] == 1:
            return False
    return True

def verifica_as_retas_da_rainha(tabuleiro, posicao):
    '''
    Esta função recebe uma matriz que representa um tabuleiro de xadrez,
    bem como a posição de uma rainha.Em seguida a função verifica se existe
    outras rainhas nas retas da posição dessa rainha, caso exista uma rainha
    em alguma reta a função retorna False, caso contrario retorna True.
    '''
    linha = posicao[0]
    coluna = posicao[1]

    # superior
    while linha != 0:
        linha -= 1
        if tabuleiro[linha][coluna] == 1:
            return False

    linha = posicao[0]

    # inferior
    while linha != 7:
        linha += 1
        if tabuleiro[linha][coluna] == 1:
            return False

    linha = posicao[0]

    # esquerda
    while coluna != 0:
        coluna -= 1
        if tabuleiro[linha][coluna] == 1:
            return False

    coluna = posicao[1]

    # direita
    while coluna != 7:
        coluna += 1
        if tabuleiro[linha][coluna] == 1:
            return False
    return True

def verificar_se_o_tabuleiro_e_solucao(entrada):
    '''
    Esta função recebe uma entrada ( string com uma sequencia de zeros
    e uns separados a cada 8 algorismo por um espaço ) que representa um
    tabuleiro de xadrez.Em seguida a função cria uma matriz que representa
    esse tabuleiro, em seguida verifica se tem 8 rainhas e 64 posições e por fim
    verifica se as rainhas não estão nas diagonais e retas umas das outras.Caso o
    tabuleiro tenha menos ou mais de 64 posições, a entrada é invalida e a
    função retorna -1.Caso uma rainha esteja na reta ou diagonal de outra,
    a entrada não é um caso de 8 rainhas e retorna 0. Caso a entrada não caia
    nos casos anteriores ela é uma entrada solução e retorna 1.

    '''
    tabuleiro = posiciona_rainhas_no_tabuleiro(entrada)
    if (verifica_se_o_tabalueiro_tem_64_posicoes(tabuleiro) and
        verifica_se_o_tabuleiro_tem_8_rainhas(tabuleiro)):
        for posicao_rainha in pega_as_posicoes_das_rainhas(tabuleiro):
            if not (verifica_as_diagonais_da_rainha(tabuleiro, posicao_rainha) and
                    verifica_as_retas_da_rainha(tabuleiro, posicao_rainha)):
                return 0
        return 1
    else:
        return -1
