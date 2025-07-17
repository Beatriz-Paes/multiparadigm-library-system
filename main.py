"""Módulo principal do sistema de biblioteca."""

from biblioteca.relatorios import Relatorios
from biblioteca.sistema import SistemaBiblioteca

# ===== COMBINAÇÃO DOS PARADIGMAS =====
# Este arquivo demonstra a combinação dos três paradigmas:
# - OO: através do uso das classes e objetos
# - Imperativo: no controle de fluxo e menus
# - Funcional: em algumas operações de processamento de dados


def menu_principal() -> str:
    """
    Exibe o menu principal e retorna a opção escolhida pelo usuário.

    Returns:
        str: Opção selecionada pelo usuário
    """
    print("\n=== Sistema de Biblioteca ===")
    print("1. Gerenciar Livros")
    print("2. Gerenciar Usuários")
    print("3. Gerenciar Empréstimos")
    print("4. Relatórios")
    print("0. Sair")
    return input("Escolha uma opção: ")


def menu_livros(sistema: SistemaBiblioteca) -> None:
    """
    Gerencia o menu de operações relacionadas a livros.

    Args:
        sistema: Instância do sistema da biblioteca
    """
    while True:
        print("\n=== Gerenciamento de Livros ===")
        print("1. Adicionar Livro")
        print("2. Buscar Livro")
        print("3. Listar Todos os Livros")
        print("4. Atualizar Livro")
        print("5. Remover Livro")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            isbn = input("ISBN: ")
            categoria = input("Categoria: ")
            sistema.adicionar_livro(titulo, autor, ano, isbn, categoria)
            print("Livro adicionado com sucesso!")

        elif opcao == "2":
            termo = input("Digite o termo de busca: ")
            livros = sistema.buscar_livros(termo)
            for livro in livros:
                print(f"\n{livro}")

        elif opcao == "3":
            for livro in sistema.listar_livros():
                print(f"\n{livro}")

        elif opcao == "4":
            isbn = input("Digite o ISBN do livro: ")
            livro_encontrado = sistema.buscar_livro_por_isbn(isbn)
            if livro_encontrado is not None:
                print("\nDados atuais:")
                print(livro_encontrado)
                titulo = input("Novo título (ou Enter para manter): ")
                autor = input("Novo autor (ou Enter para manter): ")
                sistema.atualizar_livro(isbn, titulo or None, autor or None)
                print("Livro atualizado com sucesso!")
            else:
                print("Livro não encontrado!")

        elif opcao == "5":
            isbn = input("Digite o ISBN do livro a ser removido: ")
            if sistema.remover_livro(isbn):
                print("Livro removido com sucesso!")
            else:
                print("Livro não encontrado ou não pode ser removido!")

        elif opcao == "0":
            break


def menu_usuarios(sistema: SistemaBiblioteca) -> None:
    """
    Gerencia o menu de operações relacionadas a usuários.

    Args:
        sistema: Instância do sistema da biblioteca
    """
    while True:
        print("\n=== Gerenciamento de Usuários ===")
        print("1. Cadastrar Usuário")
        print("2. Buscar Usuário")
        print("3. Listar Todos os Usuários")
        print("4. Atualizar Usuário")
        print("5. Remover Usuário")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            sistema.cadastrar_usuario(nome, email, telefone)
            print("Usuário cadastrado com sucesso!")

        elif opcao == "2":
            termo = input("Digite o termo de busca: ")
            usuarios = sistema.buscar_usuarios(termo)
            for usuario in usuarios:
                print(f"\n{usuario}")

        elif opcao == "3":
            for usuario in sistema.listar_usuarios():
                print(f"\n{usuario}")

        elif opcao == "4":
            id_usuario = int(input("Digite o ID do usuário: "))
            usuario_encontrado = sistema.buscar_usuario_por_id(id_usuario)
            if usuario_encontrado is not None:
                print("\nDados atuais:")
                print(usuario_encontrado)
                nome = input("Novo nome (ou Enter para manter): ")
                email = input("Novo email (ou Enter para manter): ")
                telefone = input("Novo telefone (ou Enter para manter): ")
                sistema.atualizar_usuario(
                    id_usuario, nome or None, email or None, telefone or None
                )
                print("Usuário atualizado com sucesso!")
            else:
                print("Usuário não encontrado!")

        elif opcao == "5":
            id_usuario = int(input("Digite o ID do usuário a ser removido: "))
            if sistema.remover_usuario(id_usuario):
                print("Usuário removido com sucesso!")
            else:
                print("Usuário não encontrado ou não pode ser removido!")

        elif opcao == "0":
            break


def menu_emprestimos(sistema: SistemaBiblioteca) -> None:
    """
    Gerencia o menu de operações relacionadas a empréstimos.

    Args:
        sistema: Instância do sistema da biblioteca
    """
    while True:
        print("\n=== Gerenciamento de Empréstimos ===")
        print("1. Realizar Empréstimo")
        print("2. Realizar Devolução")
        print("3. Listar Empréstimos Ativos")
        print("4. Verificar Atrasos")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_usuario = int(input("ID do usuário: "))
            isbn = input("ISBN do livro: ")
            dias = int(input("Quantidade de dias para devolução: "))

            if sistema.realizar_emprestimo(id_usuario, isbn, dias):
                print("Empréstimo realizado com sucesso!")
            else:
                print("Não foi possível realizar o empréstimo!")

        elif opcao == "2":
            id_emprestimo = int(input("ID do empréstimo: "))
            if sistema.realizar_devolucao(id_emprestimo):
                print("Devolução realizada com sucesso!")
            else:
                print("Não foi possível realizar a devolução!")

        elif opcao == "3":
            emprestimos = sistema.listar_emprestimos_ativos()
            for emp in emprestimos:
                print(f"\n{emp}")

        elif opcao == "4":
            atrasos = sistema.verificar_atrasos()
            if atrasos:
                print("\nEmpréstimos em atraso:")
                for emp in atrasos:
                    print(f"\n{emp}")
            else:
                print("Não há empréstimos em atraso!")

        elif opcao == "0":
            break


def menu_relatorios(sistema: SistemaBiblioteca) -> None:
    """
    Gerencia o menu de geração de relatórios.

    Args:
        sistema: Instância do sistema da biblioteca
    """
    relatorios = Relatorios(sistema)
    while True:
        print("\n=== Relatórios ===")
        print("1. Livros Mais Emprestados")
        print("2. Usuários Mais Ativos")
        print("3. Estatísticas Gerais")
        print("4. Histórico de Empréstimos")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nLivros Mais Emprestados:")
            for livro, quantidade in relatorios.livros_mais_emprestados():
                print(f"{livro.titulo}: {quantidade} empréstimos")

        elif opcao == "2":
            print("\nUsuários Mais Ativos:")
            for usuario, quantidade in relatorios.usuarios_mais_ativos():
                print(f"{usuario.nome}: {quantidade} empréstimos")

        elif opcao == "3":
            stats = relatorios.estatisticas_gerais()
            print("\nEstatísticas Gerais:")
            print(f"Total de livros: {stats['total_livros']}")
            print(f"Total de usuários: {stats['total_usuarios']}")
            print(f"Empréstimos ativos: {stats['emprestimos_ativos']}")
            print(f"Taxa de ocupação: {stats['taxa_ocupacao']:.2f}%")

        elif opcao == "4":
            print("\nHistórico de Empréstimos:")
            for emp in relatorios.historico_emprestimos():
                print(f"\n{emp}")

        elif opcao == "0":
            break


def main() -> None:
    """Função principal que inicializa e executa o sistema da biblioteca."""
    # Criação do sistema (OO)
    sistema = SistemaBiblioteca()

    # Dados de exemplo
    sistema.adicionar_livro(
        "Dom Casmurro",
        "Machado de Assis",
        1899,
        "9788535910682",
        "Literatura Brasileira",
    )
    sistema.adicionar_livro(
        "O Cortiço", "Aluísio Azevedo", 1890, "9788535910699", "Literatura Brasileira"
    )
    sistema.cadastrar_usuario("João Silva", "joao@email.com", "11999999999")
    sistema.cadastrar_usuario("Maria Santos", "maria@email.com", "11988888888")

    # Loop principal (Imperativo)
    while True:
        opcao = menu_principal()

        if opcao == "1":
            menu_livros(sistema)
        elif opcao == "2":
            menu_usuarios(sistema)
        elif opcao == "3":
            menu_emprestimos(sistema)
        elif opcao == "4":
            menu_relatorios(sistema)
        elif opcao == "0":
            print("\nObrigado por usar o Sistema de Biblioteca!")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
