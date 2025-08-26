import tkinter as tk
from tkinter import messagebox
from random import randint

def validar_nome(nome_usuario: str):
    '''
    Válida um nome informado pelo usuário 
        - deve posssuir apenas caracteres alfabeticos;
        - precisar ser maior/igual a 3 caracteres
    nome_usuario: nome que será válidado.
    return: retorna um dicionário com nome, sobrenome e nome completo válidos.
    '''

    nome = nome_usuario.strip()

    erro = ''

    # nome foi informado
    if nome:

        # lista com caracteres proibidos
        caracteres_especiais = ['.', '-', '_', '!', '?', '*', '@']
        caracter_especial = [False]

        # gerando uma lista com o nome informado
        nome_lista = nome.split()
        nome_junto = ''.join(nome_lista)

        # verificando se o nome possui caracteres especiais
        for caracter in nome_junto:

            if caracter in caracteres_especiais:
                caracter_especial[0] = True
                caracter_especial.append(caracter)

            
        # nome não possui caracteres especiais
        if caracter_especial[0] == False:

                
            # nome possue apenas letras
            if nome_junto.isalpha():

                nome_final = nome_lista[0].title()
                sobrenome_final = nome_lista[-1].title()
                nome_completo = ' '.join(nome_lista).title()


                dados = {

                    'nome_completo': nome_completo,
                    'nome': nome_final,
                    'sobrenome_final': sobrenome_final
                }
                return dados

            else:
                erro = 'O <nome> não pode possuir caracteres númericos.'


        else:
            erro = f'O <nome> não pode possuir <{caracter_especial[1:]}>.'

    
    # houve algum erro
    if erro != '':
        messagebox.showwarning(title='AVISO', message=erro)


    else:
        erro = 'O <nome> não pode ficar em branco.'

def validar_email(email_usuario: str):

    '''
    Válida um e-mail informado pelo usuário
        - deve ter apenas um '@'
        - deve ter apenas um '.' após o '@'
    email_usuario: e-mail que será válidado.
    return: retorna um e-mail válido
    '''


    email = email_usuario.strip()
    
    erro = ''

    # iniciando variaveis
    posicao_arroba = 0
    quant_arroba = 0
    posicao_primeiro_ponto = 0

    # e-mail foi informado
    if email:


        # verificando se possue apenas 1 '@'
        for indice, caracter in enumerate(email):

                if caracter == '@':
                    quant_arroba += 1
                    posicao_arroba = email_usuario.index(caracter)


        # e-mail tem apenas 1 '@'
        if quant_arroba == 1:


            # verificando a posição do primeiro '.' após o '@'
            for indice, caracter in enumerate(email):

                if  indice > posicao_arroba:

                    if caracter == '.':
                        posicao_primeiro_ponto = email.index(caracter)

                
            # e-mail com apenas 1 '.' após '@'
            if email[posicao_primeiro_ponto+1] != '.':

                return email.lower()
                
            else:
                erro = 'O <e-mail> não pode possuir mais de um "." após o "@".'


        else:
            erro = 'O <e-mail> não pode possuir mais de um "@".'

    else:
        erro = 'O <e-mail> não pode ficar em branco.'

    # houve algum erro
    if erro != '':
        messagebox.showwarning(title='AVISO', message=erro)

def validar_senha(senha_usuario: str):
    '''
    Válida a senha de algum usuário
        - deve ter no mínimo 8 caracteres
        - deve ter no mínimo 1 letra maiúscula
        - deve ter no mínimo 1 letra minúscula
        - deve ter no mínimo 1 caracter especial 
            [!, ?, #, @]
    senha_usuario: senha que será válidada.
    return: retorna uma senha válida.
    '''


    senha = senha_usuario.strip()

    erro = ''

    caracteres_especiais = ['!', '?', '#', '@']

    # inicializando variaveis
    quant_numeros = 0
    quant_maiusculas = 0
    quant_minusculas = 0
    quant_especiais = 0


    # senha informada
    if senha:

        # senha possue 8 ou mais caracteres
        if len(senha) >= 8:

            # verificando os caracteres da senha
            for caracter in senha:

                # número
                if caracter.isnumeric():
                    quant_numeros =+ 1
                    
                # letra maiúscula
                if caracter.isupper():
                    quant_maiusculas =+ 1

                # letra minuscula
                if caracter.islower():
                    quant_minusculas =+ 1

                # caracter especial
                if caracter in caracteres_especiais:
                    quant_especiais =+ 1

                # senha possue números
                if quant_numeros >= 1:

                    # senha possui maiúsculas
                    if quant_maiusculas >= 1:

                        # senha possui minúsculas
                        if quant_minusculas >= 1:

                            # senha possui caracteres especiais
                            if quant_especiais >= 1:

                                return senha
                            
                            else:
                                erro = 'A <senha> precisa possuir, no minímo, 1 caracter especial [!, ?, #, @].'

                        else:
                            erro = 'A <senha> precisa possuir, no minímo, 1 caracter em minúsculo.'

                    else:
                        erro = 'A <senha> precisa possuir, no minímo, 1 caracter em maiúsculo.'

                else:
                    erro = 'A <senha> precisa possuir, no minímo, 1 caracter númerico.'

        else:
            erro = 'A <senha> precisa ter, no minímo, 8 carcatreres.'

    else:
        erro = 'A <senha> não pode ficar em branco.'


    # houve algum erro
    if erro != '':
        messagebox.showwarning(title='AVISO', message=erro)

