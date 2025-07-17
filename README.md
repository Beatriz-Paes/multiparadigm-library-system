# Sistema de Biblioteca - Projeto Multiparadigma

![Python Version](https://img.shields.io/badge/python-3.12.11-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Este projeto é uma implementação de um sistema de gerenciamento de biblioteca que demonstra diferentes paradigmas de programação (Orientado a Objetos, Imperativo e Funcional) usando Python.

## 📚 Sobre o Projeto

O sistema permite gerenciar uma biblioteca, incluindo:
- Cadastro e gerenciamento de livros
- Cadastro e gerenciamento de usuários
- Controle de empréstimos e devoluções
- Geração de relatórios e estatísticas

### Paradigmas Implementados

1. **Paradigma Orientado a Objetos**
    - Modelagem de entidades (Livro, Usuário, Empréstimo)
   - Encapsulamento de dados e comportamentos
   - Relacionamentos entre classes
   - Polimorfismo

2. **Paradigma Imperativo**
   - Controle de fluxo com estruturas condicionais
   - Modificação direta de estado
   - Sequência de operações definidas
   - Interface de usuário por linha de comando

3. **Paradigma Funcional**
   - Processamento de coleções de forma funcional
   - Funções puras para relatórios
   - List comprehensions
   - Funções lambda

## 🛠️ Tecnologias Utilizadas
- Python 3.12.11
- Bibliotecas padrão Python:
    - `dataclasses`
    - `datetime`
    - `typing`
    - `collections`

### Dependências de Desenvolvimento
- `pre-commit`
- `black`
- `flake8`
- `isort`
- `mypy`


## 📁 Estrutura do Projeto
```plaintext
    projeto_biblioteca/
    ├── biblioteca/
    │   ├── __init__.py
    │   ├── models.py     # Classes e modelos (OO)
    │   ├── sistema.py    # Lógica do sistema (Imperativo)
    │   └── relatorios.py # Geração de relatórios (Funcional)
    ├── tests/            # Testes unitários (a ser implementado)
    ├── .flake8          # Configuração do flake8
    ├── .gitignore       # Arquivos ignorados pelo git
    ├── .pre-commit-config.yaml
    ├── main.py          # Interface do usuário
    ├── pyproject.toml   # Configuração do black e outras ferramentas
    ├── README.md
    ├── requirements-dev.txt
    └── setup.cfg        # Configurações de desenvolvimento
```


## 🚀 Como Executar

1. **Requisitos**
   - Python 3.12.11 ou superior
   - Git instalado

2. **Configuração Básica**
   ```bash
   # Clone o repositório
   git clone [url-do-repositorio]

   # Entre no diretório
   cd projeto_biblioteca

   # Crie e ative um ambiente virtual
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   # ou
   .\venv\Scripts\activate  # Windows

   # Instale as dependências do projeto
   pip install -r requirements.txt

   # Instale as dependências de desenvolvimento (opcional)
   pip install -r requirements-dev.txt
   ```

3. **Execução**
   ```bash
   python main.py
   ```

## 🔧 Desenvolvimento

Se você deseja contribuir ou desenvolver o projeto, siga estas etapas adicionais:

1. **Instale as dependências de desenvolvimento**
   ```bash
   pip install -r requirements-dev.txt
   ```

2. **Configure o pre-commit**
   ```bash
   pre-commit install
   ```

### Ferramentas de Qualidade de Código

O projeto utiliza as seguintes ferramentas para garantir a qualidade do código:

- **black**: Formatação de código
- **flake8**: Linting
- **isort**: Organização de imports
- **mypy**: Verificação de tipos estática
- **pre-commit**: Hooks de git para verificações automáticas

Para executar todas as verificações manualmente:
```bash
pre-commit run --all-files
```


## 💻 Funcionalidades

### Gerenciamento de Livros
- Adicionar novos livros
- Buscar livros por título, autor ou ISBN
- Atualizar informações dos livros
- Remover livros do acervo

### Gerenciamento de Usuários
- Cadastrar novos usuários
- Buscar usuários por nome ou email
- Atualizar dados dos usuários
- Remover usuários do sistema

### Controle de Empréstimos
- Realizar empréstimos
- Registrar devoluções
- Verificar atrasos
- Listar empréstimos ativos

### Relatórios
- Livros mais emprestados
- Usuários mais ativos
- Estatísticas gerais
- Histórico de empréstimos

## 📊 Exemplos de Uso
```python
    # Criar um novo livro
    sistema.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899, "9788535910682", "Literatura Brasileira")
    # Cadastrar um usuário
    sistema.cadastrar_usuario("João Silva", "joao@email.com", "11999999999")
    # Realizar um empréstimo
    sistema.realizar_emprestimo(id_usuario=1, isbn="9788535910682", dias=14)
```

## 🎯 Conceitos Demonstrados

### Orientação a Objetos
- Encapsulamento de dados
- Composição entre classes
- Polimorfismo através de sobrescrita de métodos
- Relacionamentos entre entidades

### Programação Imperativa
- Controle de fluxo com if/else
- Modificação de estado
- Loops e iterações
- Sequência de instruções

### Programação Funcional
- Funções puras
- Processamento de coleções
- List comprehensions
- Funções de ordem superior

## 👥 Contribuição

Este projeto foi desenvolvido como demonstração de diferentes paradigmas de programação. Contribuições são bem-vindas para:
- Melhorias na interface do usuário
- Adição de novas funcionalidades
- Otimização do código
- Documentação adicional

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
