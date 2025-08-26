# 📚 Sistema de Cadastro de Alunos - Senac Minas

Este é um projeto em **Python** utilizando CustomTkinter para interface gráfica e **SQLite** como banco de dados.
Foi desenvolvido de forma independente como prática durante o curso Técnico em Informática no **Senac Minas**.

---

## 🔧 Tecnologias Utilizadas

- Python
- SQLite3
- CustomTkinter
- Tkinter/Messagebox

---

## 📌 Funcionalidades

O sistema possui as seguintes funcionalidades:
- ✅ **Cadastrar aluno** (com validação de nomes, e-mail, curso e senha)
- ✅ **Geração automática de login** (com base no nome informado)
- ✅ **Login de usuário** (com validação de credenciais)

---

## 🗃️ Estrutura da Tabela no Banco de Dados

A tabela `alunos` possui os seguintes campos:

| Campo            | Tipo     | Regras                                                        |
|------------------|----------|---------------------------------------------------------------|
| `cod_aluno`      | INTEGER  | Chave primária, autoincrementável                             |
| `usuario`        | TEXT     | Obrigatório, único, gerado automaticamente                    |
| `email`          | TEXT     | Obrigatório, único                                            |
| `senha`          | TEXT     | Obrigatório                                                   |
| `curso`          | TEXT     | Obrigatório                                                   |

---

## 🧩 Organização do Projeto

- `banco.py` – Conexão e criação da tabela no banco SQLite.
- `cadastro.py` – Tela de cadastro de usuários.
- `login.py` – Tela de login de usuários.
- `funcoes.py` – Funções auxiliares para validação (nome, e-mail, senha).
- `monitoria da 49.db` – Banco de dados SQLite.
- `requirements.txt` – Dependências do projeto.

---

## ▶️ Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/maicnv/monitoria-da-49-cadastro-login
