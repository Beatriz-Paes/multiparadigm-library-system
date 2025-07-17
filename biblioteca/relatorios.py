"""Módulo de relatórios do sistema de biblioteca."""

from collections import Counter
from typing import List, Tuple

from biblioteca.models import Emprestimo, Livro, Usuario
from biblioteca.sistema import SistemaBiblioteca

# ===== PARADIGMA FUNCIONAL =====
# Este arquivo demonstra o paradigma funcional através de:
# - Funções puras que não modificam estado
# - Uso de funções de ordem superior (map, filter, sorted)
# - Processamento de coleções de forma funcional
# - Uso de expressões lambda


class Relatorios:
    """Classe responsável por gerar relatórios do sistema de biblioteca."""

    def __init__(self, sistema: SistemaBiblioteca) -> None:
        """Inicializa a classe Relatorios com o sistema de biblioteca."""
        self.sistema = sistema

    def livros_mais_emprestados(self) -> List[Tuple[Livro, int]]:
        """Retorna lista dos livros mais emprestados ordenada por quantidade.

        Returns:
            List[Tuple[Livro, int]]: Lista de tuplas com (livro, quantidade_emprestimos)
                ordenada de forma decrescente por quantidade.
        """
        # Exemplo de programação funcional:
        # - Uso de funções de ordem superior (Counter)
        # - Transformação de dados sem modificar estado
        contagem = Counter(emp.livro for emp in self.sistema.emprestimos)
        return sorted(
            contagem.items(), key=lambda x: x[1], reverse=True  # Função lambda
        )

    def usuarios_mais_ativos(self) -> List[Tuple[Usuario, int]]:
        """Retorna lista dos usuários mais ativos ordenada.

        Returns:
            List[Tuple[Usuario, int]]: Lista de tuplas com
            (usuario, quantidade_emprestimos)
                ordenada de forma decrescente por quantidade.
        """
        # Outro exemplo de processamento funcional de dados
        contagem = Counter(emp.usuario for emp in self.sistema.emprestimos)
        return sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    def estatisticas_gerais(self) -> dict[str, float]:
        """Retorna estatísticas gerais do sistema.

        Returns:
            dict[str, float]: Dicionário com estatísticas:
                - total_livros: número total de livros
                - total_usuarios: número total de usuários
                - emprestimos_ativos: número de empréstimos ativos
                - taxa_ocupacao: percentual de livros emprestados
        """
        # Uso de list comprehension (característica funcional)
        total_livros = len(self.sistema.livros)
        livros_emprestados = len(
            [livro for livro in self.sistema.livros if not livro.disponivel]
        )

        return {
            "total_livros": total_livros,
            "total_usuarios": len(self.sistema.usuarios),
            "emprestimos_ativos": len(self.sistema.listar_emprestimos_ativos()),
            "taxa_ocupacao": (
                (livros_emprestados / total_livros * 100) if total_livros > 0 else 0
            ),
        }

    def historico_emprestimos(self) -> List[Emprestimo]:
        """Retorna histórico completo de empréstimos ordenado por data.

        Returns:
            List[Emprestimo]: Lista de empréstimos ordenada por data_emprestimo
                de forma decrescente (mais recentes primeiro).
        """
        # Exemplo de transformação funcional com sorted e lambda
        return sorted(
            self.sistema.emprestimos, key=lambda x: x.data_emprestimo, reverse=True
        )
