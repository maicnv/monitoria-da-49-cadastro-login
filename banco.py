import sqlite3
from random import randint
from tkinter import messagebox

class Banco():

    # inicializando os atributos
    def __init__(self, nome_banco):
        
        self.banco = nome_banco
        self.conexao = None

    # conectar no banco 
    def conectar(self):
        '''
        Conecta ao banco de dados (se ele não existir, um é criado).
        '''
        
        try:
            conexao = sqlite3.connect(self.banco)

        except sqlite3.Error as erro:
            #messagebox.showerror(title='ERRO', message='Não foi possível se conectar ao banco de dados.')

            print(erro)

        else:
            return conexao
        

class Tabela():

    def __init__(self):
        pass

    # criar tebela
    def criar_tabela(self):
        '''
        Cria uma tabela 'usuarios' no banco de dados.
            - cod_aluno;
            - usuario;
            - email;
            - senha;
            - curso;
        '''

        # conectando no banco
        banco = Banco('monitoria da 49.db')
        monitoria = banco.conectar()


        # criando a tabela
        try:

            monitoria.execute(
                    
         
            '''
                CREATE TABLE IF NOT EXISTS usuarios (
                    
                cod_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                curso TEXT NOT NULL
            
                )
                
            '''

            )

        except Exception as erro:
            print(erro)

        else:
            monitoria.commit()

        finally:
            monitoria.close()

    

    def gerar_login(self, nome_usuario):

        # dados para gerar o login
        lista_nome = nome_usuario.split()
        primeira_letra = lista_nome[0][0]
        sobrenome = lista_nome[-1].upper()

        while True:

            digito = str(randint(0, 2))
            monitoria = Banco('monitoria da 49.db')

            # gerando o login
            login_lista = [primeira_letra, sobrenome, digito]
            login_final = ''.join(login_lista)


            # pegando todos os usuarios do app
            banco = monitoria.conectar()
            
            logins = banco.execute(

                '''
                SELECT usuario FROM usuarios
                '''
                
            )
        

            # verificando se o login gerado já existe
            if login_final not in logins:

                return login_final

            else:
                digito = str(randint(0, 10))

    def verificar_email(self, email_usuario):
        '''
        Verifica se um e-mail já está cadastrado no banco de dados.
        email_usuario: e-mail que será verificado
        retiurn: retorna 
            - 'True' para e-mail já cadastrado 
            - 'False' para e-mail não cadastrado
        '''

        # conectabdo ao banco
        try:

            monitoria = Banco('monitoria da 49.db')
            banco = monitoria.conectar()

        except:

            messagebox.showerror(title='ERRO', message='Houve um <erro ao conectar> no banco de dados. Tente novamente mais tarde.')

        else:

            # pegando os e-mails cadastrados no banco
            emails = banco.execute(

                '''
                SELECT email FROM usuarios
                '''
            ) 

            # aduicionando os e-mails em uma lista
            lista_emails = []
            for email in emails:
                lista_emails.append(email[0])

            # verificando se o email existe
            if email_usuario in lista_emails:
                return True

            else:
                return False

        finally:

            banco.close()           
