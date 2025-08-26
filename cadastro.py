import customtkinter as ctk
from funcoes import *
from banco import *


# criando o app
app = ctk.CTk()
app.geometry('500x400')
app.resizable(False, False)

# modificando o app
app.title('Cadastro')
app._set_appearance_mode('dark')

# função para gerar o cadastro
def gerar_cadastro():
    '''
    Válida um cadastro no app.
        - adicona um usuário ao banco de dados
    return: retorna um dicionário com nome, email, curso e senha do usuário.
    '''


    try:
        
        # pegando os dados passados
        nome = validar_nome(nome_usuario=campo_nome.get())
        email = validar_email(email_usuario=campo_email.get())
        curso = campo_curso.get()
        senha = validar_senha(senha_usuario=campo_senha.get())
        confirmar_senha = validar_senha(senha_usuario=campo_confirmar_senha.get())

    
    except:
        messagebox.showerror(title='ERRO', message='Houve um <erro inesperado> ao coletar os dados. Tente novamente mais tarde.')

    else:

        # verificando se as senhas são iguais
        if senha == confirmar_senha:
            
            # gerando o obejto 'usuario'
            usuario = {

                'nome': nome,
                'email': email,
                'curso': curso,
                'senha': senha
            }
            
            # verificando se o email já esta cadastrado
            tabela = Tabela()
            vemail = tabela.verificar_email(email_usuario=email)

            # e-mail não cadastrado
            if vemail == False:

            
                # gerando o login
                nome = usuario['nome']['nome_completo']
                login = tabela.gerar_login(nome_usuario=nome)

                
                # gerou o login
                if login:

                    monitoria = Banco('monitoria da 49.db')
                    banco = monitoria.conectar()

                    try:

                        # cadastrando os dados
                        banco.execute(

                            '''
                            INSERT INTO usuarios (usuario, email, senha, curso)
                            VALUES (?, ?, ?, ?)
                            ''', (login, email, senha, curso)
                        )

                    except:
                        messagebox.showerror(title='ERRO', message='Houve um <erro inesperado> ao gerar o cadastro. Tente novamente mais tarde.')

                    else:

                        messagebox.showinfo(title='AVISO', message=f'Cadastrado realizado com sucesso! Seu login é: <{login}>.')
                        banco.commit()

                    finally:

                        banco.close()

            else:
                messagebox.showwarning(title='AVISO', message='O <email> informado já está cadastrado. Tente novamente com outro.')

        else:
            messagebox.showerror(title='ERRO', message='As <senhas> não coincidem.')


# fonte padrão do app
fonte_padrao = ('System', 12)
fonte_padrao_dois = ('System', 15)

# titulo do app
titulo_principal = ctk.CTkLabel(master=app, width=100, text='Monitoria da 49', font=('System', 30, 'bold'))
titulo_nome = ctk.CTkLabel(master=app, width=50, text='Nome', font=fonte_padrao)
titulo_sobrenome = ctk.CTkLabel(master=app, width=50, text='Sobrenome', font=fonte_padrao)
titulo_curso = ctk.CTkLabel(master=app, width=50, text='Curso', font=fonte_padrao)
titulo_email = ctk.CTkLabel(master=app, width=50, text='E-mail', font=fonte_padrao)
titulo_senha = ctk.CTkLabel(master=app, width=50, text='Senha', font=fonte_padrao)
titulo_confirmar_senha = ctk.CTkLabel(master=app, width=50, text='Confirmar Senha', font=fonte_padrao)


# campos
campo_nome = ctk.CTkEntry(master=app, width=450, font=fonte_padrao_dois)

cursos_disponiveis = [

    'Téc. Administração',
    'Téc. Contabilidade',
    'Téc. Desenvolvimento de Sistemas',
    'Téc. Enfermagem',
    'Téc. Eventos',
    'Téc. Guia de Turismo',
    'Téc. Informática',
    'Téc. Instrumentação Cirúrgica',
    'Téc. Logística',
    'Téc. Produção de Moda',
    'Téc. Redes de Computadores',
    'Téc. Segurança do Trabalho'
]
campo_curso = ctk.CTkComboBox(master=app, values=cursos_disponiveis, width=450, font=fonte_padrao_dois)

campo_email = ctk.CTkEntry(master=app, width=450, font=fonte_padrao_dois)

campo_senha = ctk.CTkEntry(master=app, width=200, font=fonte_padrao_dois, show='*')

campo_confirmar_senha = ctk.CTkEntry(master=app, width=200, font=fonte_padrao_dois, show='*')

# botao
botao_cadastro = ctk.CTkButton(master=app, width=100, text='CADASTRAR', font=('System', 15, 'bold'), command=gerar_cadastro)

# mostrando na tela
titulo_principal.place(relx=0.5, y=20, anchor='center')

titulo_nome.place(relx=0.135, y=70, anchor='e')
campo_nome.place(relx=0.5, y =90, anchor='center')

titulo_curso.place(relx=0.135, y=140, anchor='e')
campo_curso.place(relx=0.5, y=160, anchor='center')
campo_curso.set('')

titulo_email.place(relx=0.135, y=210, anchor='e')
campo_email.place(relx=0.5, y=230, anchor='center')

titulo_senha.place(relx=0.135, y=280, anchor='e')
campo_senha.place(relx=0.25, y=300, anchor='center')

titulo_confirmar_senha.place(relx=0.720, y=280, anchor='e')
campo_confirmar_senha.place(relx=0.75, y=300, anchor='center')

botao_cadastro.place(relx=0.5, y=370, anchor='center')

app.mainloop()
