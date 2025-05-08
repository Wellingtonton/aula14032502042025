class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}"

class Usuario:
    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario

    def __str__(self):
        return f"Nome: {self.nome}, ID: {self.id_usuario}"

class Emprestimo:
    def __init__(self, livro, usuario, data_emprestimo, data_devolucao):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def __str__(self):
        return f"Livro: {self.livro.titulo}, Usuário: {self.usuario.nome}, Empréstimo: {self.data_emprestimo}, Devolução: {self.data_devolucao}"

class SistemaBiblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def cadastrar_livro(self, titulo, autor, isbn):
        livro = Livro(titulo, autor, isbn)
        self.livros.append(livro)
        print(f"Livro '{titulo}' cadastrado com sucesso.")

    def cadastrar_usuario(self, nome, id_usuario):
        usuario = Usuario(nome, id_usuario)
        self.usuarios.append(usuario)
        print(f"Usuário '{nome}' cadastrado com sucesso.")

    def cadastrar_emprestimo(self, livro, usuario, data_emprestimo, data_devolucao):
        if livro in self.livros and usuario in self.usuarios:
            emprestimo = Emprestimo(livro, usuario, data_emprestimo, data_devolucao)
            self.emprestimos.append(emprestimo)
            print(f"Empréstimo do livro '{livro.titulo}' para '{usuario.nome}' cadastrado com sucesso.")
        else:
            print("Livro ou usuário não encontrado.")

    def consultar_livros(self):
        if self.livros:
            print("\n--- Livros Cadastrados ---")
            for livro in self.livros:
                print(livro)
        else:
            print("Nenhum livro cadastrado.")

    def consultar_usuarios(self):
        if self.usuarios:
            print("\n--- Usuários Cadastrados ---")
            for usuario in self.usuarios:
                print(usuario)
        else:
            print("Nenhum usuário cadastrado.")

# Exemplo de uso do sistema
biblioteca = SistemaBiblioteca()

# Cadastrando livros
biblioteca.cadastrar_livro("Dom Quixote", "Miguel de Cervantes", "978-85-7232-800-5")
biblioteca.cadastrar_livro("1984", "George Orwell", "978-85-254-2208-0")

# Cadastrando usuários
biblioteca.cadastrar_usuario("Maria Silva", "MS123")
biblioteca.cadastrar_usuario("João Pereira", "JP456")

# Consultando livros e usuários
biblioteca.consultar_livros()
biblioteca.consultar_usuarios()

# Criando um empréstimo (precisamos referenciar os objetos já cadastrados)
livro1 = biblioteca.livros[0]
usuario1 = biblioteca.usuarios[0]
biblioteca.cadastrar_emprestimo(livro1, usuario1, "2025-05-10", "2025-05-20")

# Podemos adicionar mais funcionalidades depois, como consultar empréstimos, realizar devoluções, etc.