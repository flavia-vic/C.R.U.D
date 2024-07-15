# C.R.U.D
Este projeto é uma aplicação Flask simples que utiliza uma classe Database para se conectar a um banco de dados MySQL e realizar operações CRUD (Create, Read, Update, Delete) em uma tabela de estudantes. A seguir, uma breve explicação das funcionalidades principais:

## funções principais	
### Classe Database (arquivo con.py)
A classe Database facilita a conexão e operações com o banco de dados MySQL:

- Conexão: Permite conectar-se ao banco de dados especificado através dos parâmetros de usuário, senha, nome do banco de dados e host.

- Operações de Leitura:
read_students(): Retorna todos os estudantes da tabela estudantes.
read_students_paginate(page, per_page): Retorna uma página específica de estudantes com paginação.

- Operações de Atualização e Remoção:
atualizar_estudante_no_banco(student_id, data): Atualiza um estudante específico pelo ID com os dados fornecidos.
deletar_estudante(student_id): Remove um estudante da tabela pelo ID fornecido.

- Operação de Inserção:

inserir_estudante(data): Insere um novo estudante na tabela com os dados fornecidos.

Aplicação Flask (arquivo main.py)

A aplicação Flask utiliza a classe Database para criar uma API RESTful que oferece os seguintes endpoints:
- /conectar (POST): Conecta-se ao banco de dados MySQL utilizando parâmetros fornecidos via POST.
- /ler (GET): Retorna todos os estudantes da tabela estudantes.
- /ler_por_pagina (GET): Retorna uma página específica de estudantes com paginação.
- /atualizar_estudante/<student_id> (PUT): Atualiza os dados de um estudante específico pelo ID.
- /deletar-por-id/<id> (DELETE): Remove um estudante da tabela pelo ID.
- /inserir-estudante (POST): Insere um novo estudante na tabela com os dados fornecidos via POST.

## Configuração e Execução
Para executar o projeto localmente:

- Instale as bibliotecas necessárias.
- Execute o arquivo main.py.
- Acesse os endpoints definidos para realizar operações no banco de dados, podendo ser acessados com ferramentas como Postman e Insomnia.