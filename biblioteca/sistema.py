"""Módulo do sistema de biblioteca que implementa o paradigma imperativo."""

from datetime import datetime, timedelta
from typing import List, Optional

from biblioteca.models import Emprestimo, Livro, Usuario

# ===== PARADIGMA IMPERATIVO =====
# Este arquivo demonstra o paradigma imperativo através de:
# - Modificação direta de estado
# - Sequência de instruções
# - Estruturas de controle (if/else, loops)
# - Comandos que alteram o estado do programa


class SistemaBiblioteca:
    """Classe que representa o sistema de biblioteca."""

    def __init__(self) -> None:
        """Inicializa o sistema de biblioteca com listas vazias e IDs iniciais."""
        # Estado do sistema mantido em variáveis (característica imperativa)
        self.livros: List[Livro] = []
        self.usuarios: List[Usuario] = []
        self.emprestimos: List[Emprestimo] = []
        self.proximo_id_usuario = 1
        self.proximo_id_emprestimo = 1

    # Métodos imperativos que modificam o estado do sistema
    def adicionar_livro(
        self, titulo: str, autor: str, ano: int, isbn: str, categoria: str
    ) -> Livro:
        """Adiciona um novo livro ao sistema.

        Args:
            titulo: Título do livro
            autor: Nome do autor
            ano: Ano de publicação
            isbn: ISBN do livro
            categoria: Categoria do livro

        Returns:
            Livro: O objeto livro criado e adicionado ao sistema
        """
        livro = Livro(titulo, autor, ano, isbn, categoria)
        self.livros.append(livro)  # Modificação direta do estado
        return livro

    def buscar_livros(self, termo: str) -> List[Livro]:
        """Busca livros que contenham o termo especificado no título, autor ou ISBN.

        Args:
            termo: Termo de busca

        Returns:
            List[Livro]: Lista de livros que correspondem ao critério de busca
        """
        termo = termo.lower()
        return [
            livro
            for livro in self.livros
            if termo in livro.titulo.lower()
            or termo in livro.autor.lower()
            or termo in livro.isbn.lower()
        ]

    def buscar_livro_por_isbn(self, isbn: str) -> Optional[Livro]:
        """Busca um livro pelo seu ISBN.

        Args:
            isbn: ISBN do livro

        Returns:
            Optional[Livro]: O livro encontrado ou None se não existir
        """
        return next((livro for livro in self.livros if livro.isbn == isbn), None)

    def atualizar_livro(
        self, isbn: str, titulo: Optional[str] = None, autor: Optional[str] = None
    ) -> bool:
        """Atualiza as informações de um livro existente.

        Args:
            isbn: ISBN do livro a ser atualizado
            titulo: Novo título do livro (opcional)
            autor: Novo autor do livro (opcional)

        Returns:
            bool: True se o livro foi atualizado com sucesso, False caso contrário
        """
        livro = self.buscar_livro_por_isbn(isbn)
        if livro:
            if titulo:
                livro.titulo = titulo
            if autor:
                livro.autor = autor
            return True
        return False

    def remover_livro(self, isbn: str) -> bool:
        """Remove um livro do sistema se ele estiver disponível.

        Args:
            isbn: ISBN do livro a ser removido

        Returns:
            bool: True se o livro foi removido com sucesso, False caso contrário
        """
        livro = self.buscar_livro_por_isbn(isbn)
        if livro and livro.disponivel:
            self.livros.remove(livro)
            return True
        return False

    def listar_livros(self) -> List[Livro]:
        """Lista todos os livros cadastrados no sistema.

        Returns:
            List[Livro]: Lista com todos os livros do sistema
        """
        return self.livros

    # Métodos para gerenciamento de usuários
    def cadastrar_usuario(self, nome: str, email: str, telefone: str) -> Usuario:
        """Cadastra um novo usuário no sistema.

        Args:
            nome: Nome do usuário
            email: Email do usuário
            telefone: Telefone do usuário

        Returns:
            Usuario: O objeto usuário criado e cadastrado no sistema
        """
        usuario = Usuario(self.proximo_id_usuario, nome, email, telefone)
        self.usuarios.append(usuario)
        self.proximo_id_usuario += 1
        return usuario

    def buscar_usuarios(self, termo: str) -> List[Usuario]:
        """Busca usuários que contenham o termo especificado no nome ou email.

        Args:
            termo: Termo de busca

        Returns:
            List[Usuario]: Lista de usuários que correspondem ao critério de busca
        """
        termo = termo.lower()
        return [
            u
            for u in self.usuarios
            if termo in u.nome.lower() or termo in u.email.lower()
        ]

    def buscar_usuario_por_id(self, id_usuario: int) -> Optional[Usuario]:
        """Busca um usuário pelo seu ID.

        Args:
            id_usuario: ID do usuário

        Returns:
            Optional[Usuario]: O usuário encontrado ou None se não existir
        """
        return next((u for u in self.usuarios if u.id == id_usuario), None)

    def atualizar_usuario(
        self,
        id_usuario: int,
        nome: Optional[str] = None,
        email: Optional[str] = None,
        telefone: Optional[str] = None,
    ) -> bool:
        """Atualiza as informações de um usuário existente.

        Args:
            id_usuario: ID do usuário a ser atualizado
            nome: Novo nome do usuário (opcional)
            email: Novo email do usuário (opcional)
            telefone: Novo telefone do usuário (opcional)

        Returns:
            bool: True se o usuário foi atualizado com sucesso, False caso contrário
        """
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario:
            if nome:
                usuario.nome = nome
            if email:
                usuario.email = email
            if telefone:
                usuario.telefone = telefone
            return True
        return False

    def remover_usuario(self, id_usuario: int) -> bool:
        """Remove um usuário do sistema se ele não tiver empréstimos ativos.

        Args:
            id_usuario: ID do usuário a ser removido

        Returns:
            bool: True se o usuário foi removido com sucesso, False caso contrário
        """
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario and not usuario.emprestimos_ativos:
            self.usuarios.remove(usuario)
            return True
        return False

    def listar_usuarios(self) -> List[Usuario]:
        """Lista todos os usuários cadastrados no sistema.

        Returns:
            List[Usuario]: Lista com todos os usuários do sistema
        """
        return self.usuarios

    # Métodos para gerenciamento de empréstimos
    def realizar_emprestimo(self, id_usuario: int, isbn: str, dias: int) -> bool:
        """Realiza o empréstimo de um livro para um usuário.

        Args:
            id_usuario: ID do usuário que está pegando o livro emprestado
            isbn: ISBN do livro a ser emprestado
            dias: Número de dias do empréstimo

        Returns:
            bool: True se o empréstimo foi realizado com sucesso, False caso contrário
        """
        # Exemplo de controle de fluxo imperativo
        usuario = self.buscar_usuario_por_id(id_usuario)
        livro = self.buscar_livro_por_isbn(isbn)

        if not usuario or not livro or not livro.disponivel:
            return False

        if len(usuario.emprestimos_ativos) >= 3:
            return False

        # Sequência de operações que modificam o estado
        emprestimo = Emprestimo(
            id=self.proximo_id_emprestimo,
            usuario=usuario,
            livro=livro,
            data_emprestimo=datetime.now(),
            data_prevista_devolucao=datetime.now() + timedelta(days=dias),
        )

        self.emprestimos.append(emprestimo)
        usuario.emprestimos_ativos.append(emprestimo)
        livro.disponivel = False
        self.proximo_id_emprestimo += 1

        return True

    def realizar_devolucao(self, id_emprestimo: int) -> bool:
        """Realiza a devolução de um livro emprestado.

        Args:
            id_emprestimo: ID do empréstimo a ser finalizado

        Returns:
            bool: True se a devolução foi realizada com sucesso, False caso contrário
        """
        emprestimo = next(
            (
                e
                for e in self.emprestimos
                if e.id == id_emprestimo and not e.data_devolucao
            ),
            None,
        )
        if not emprestimo:
            return False

        emprestimo.data_devolucao = datetime.now()
        emprestimo.livro.disponivel = True
        emprestimo.usuario.emprestimos_ativos.remove(emprestimo)

        return True

    def listar_emprestimos_ativos(self) -> List[Emprestimo]:
        """Lista todos os empréstimos ativos no sistema.

        Returns:
            List[Emprestimo]: Lista de empréstimos que ainda não foram devolvidos
        """
        return [e for e in self.emprestimos if not e.data_devolucao]

    def verificar_atrasos(self) -> List[Emprestimo]:
        """Verifica todos os empréstimos ativos que estão em atraso.

        Returns:
            List[Emprestimo]: Lista de empréstimos ativos que estão em atraso
        """
        return [
            e for e in self.emprestimos if not e.data_devolucao and e.esta_atrasado()
        ]
