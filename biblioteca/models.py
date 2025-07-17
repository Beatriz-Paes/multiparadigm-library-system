"""Módulo de modelos do sistema de biblioteca."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

# ===== PARADIGMA ORIENTADO A OBJETOS =====
# Este arquivo demonstra os principais conceitos de OO:
# - Encapsulamento: através das classes e seus atributos
# - Composição: relacionamentos entre as classes
# - Polimorfismo: através da sobrescrita de métodos como __str__


@dataclass
class Livro:
    """Classe que representa um livro na biblioteca."""

    titulo: str
    autor: str
    ano: int
    isbn: str
    categoria: str
    disponivel: bool = True

    def __str__(self) -> str:  # Polimorfismo através da sobrescrita em __str__
        """Representação textual do livro."""
        status = "Disponível" if self.disponivel else "Emprestado"
        return (
            f"Livro: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}\n"
            f"ISBN: {self.isbn}\nCategoria: {self.categoria}\nStatus: {status}"
        )


@dataclass
class Usuario:
    """Classe que representa um usuário do sistema de biblioteca."""

    id: int
    nome: str
    email: str
    telefone: str
    ativo: bool = True
    # Exemplo de composição: Usuario possui uma lista de empréstimos
    emprestimos_ativos: List["Emprestimo"] = field(default_factory=list)

    def __str__(self) -> str:
        """Representação textual do usuário."""
        return (
            f"ID: {self.id}\nNome: {self.nome}\nEmail: {self.email}\n"
            f"Telefone: {self.telefone}\n"
            f"Empréstimos ativos: {len(self.emprestimos_ativos)}"
        )


@dataclass
class Emprestimo:
    """Classe que representa um empréstimo de livro."""

    id: int
    usuario: Usuario  # Relacionamento com Usuario
    livro: Livro  # Relacionamento com Livro
    data_emprestimo: datetime
    data_prevista_devolucao: datetime
    data_devolucao: Optional[datetime] = None

    # Encapsula a lógica de negócio (outro exemplo de encapsulamento)
    def esta_atrasado(self) -> bool:
        """Verifica se o empréstimo está atrasado."""
        if self.data_devolucao:
            return self.data_devolucao > self.data_prevista_devolucao
        return datetime.now() > self.data_prevista_devolucao

    def __str__(self) -> str:
        """Representação textual do empréstimo."""
        status = "Devolvido" if self.data_devolucao else "Em andamento"
        atraso = " (Em atraso)" if self.esta_atrasado() else ""
        return (
            f"ID: {self.id}\nLivro: {self.livro.titulo}\n"
            f"Usuário: {self.usuario.nome}\n"
            f"Data empréstimo: {self.data_emprestimo.strftime('%d/%m/%Y')}\n"
            f"Previsão devolução: {self.data_prevista_devolucao.strftime('%d/%m/%Y')}\n"
            f"Status: {status}{atraso}"
        )
