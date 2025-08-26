import customtkinter as ctk
from funcoes import *
from banco import *


# criando o app
app = ctk.CTk()
app.geometry('250x250')
app.resizable('False', 'False')

# modificando o app
app.title('Login')
app._set_appearance_mode('dark')

# função para verificar o login
def verificar_login():

    # pegando os dados informados
    login_usuario = campo_login.get().upper()
    senha_usuario = campo_senha.get()


    # conectando ao banco
    try:

        banco = Banco('monitoria da 49.db')
        monitoria = banco.conectar()

    except Exception as erro:
        print(erro)

    else:

        # pegando todos os logins
        logins = monitoria.execute(

            '''
            SELECT usuario FROM usuarios
            '''
        )

        # adicionando os logins em uma lista
        lista_logins = []
        for login in logins:

            lista_logins.append(login[0])


        # o login informado existe
        if login_usuario in lista_logins:
            
            # pegando a senha do sistema
            senha_sistema = monitoria.execute(

                '''
                SELECT senha FROM usuarios
                WHERE usuario = ?
                ''',(login_usuario,)
            )
            
            # adicionando a senha real em uma lista
            lista_senha = []
            for senha in senha_sistema:
                lista_senha.append(senha[0])


            # verificando se a senha informada é a mesma do sistema
            if senha_usuario in lista_senha:
                messagebox.showinfo(title='ACESSO LIBERADO', message=f'Olá <{login_usuario}>, bem-vindo(a) a aplicação de Monitoria da turma 49!')

            else:
                messagebox.showerror(title='ACESSO NEGADO', message='Sua senha está incorreta.')

        else:
          messagebox.showwarning(title='ACESSO NEGADO', message='Login inexiste.')

# titulo do app
titulo_principal = ctk.CTkLabel(master=app, width=400, text='Monitoria da 49', font=('System', 20, 'bold'))
titulo_login = ctk.CTkLabel(master=app, width=50, text='Login', font=('System', 12, 'bold'))
titulo_senha = ctk.CTkLabel(master=app, width=50, text='Senha', font=('System', 12, 'bold'))

# campos
campo_login = ctk.CTkEntry(master=app, width=200, font=('System', 15))
campo_senha = ctk.CTkEntry(master=app, width=200, font=('System', 15), show='*')

# botao
botao_login = ctk.CTkButton(master=app, width=100, text='LOGIN', font=('System', 15, 'bold'), command=verificar_login)

# mostrando na tela
titulo_principal.place(relx=0.5, y=20, anchor='center')

titulo_login.place(relx=0.17, y=58, anchor='center')
campo_login.place(relx=0.5, y=80, anchor='center')

titulo_senha.place(relx=0.17, y=118, anchor='center')
campo_senha.place(relx=0.5, y=140, anchor='center')

botao_login.place(relx=0.5, y=200, anchor='center')

app.mainloop()
