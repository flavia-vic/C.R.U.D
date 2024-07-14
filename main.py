import mysql.connector
from mysql.connector import Error

# Função para conectar ao banco de dados
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="192.168.1.10",
            user="pi",
            password="raspberry",
            database="random"
        )
        if connection.is_connected():
            print("Conexão bem-sucedida!")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para fechar a conexão
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexão fechada.")

# Função para criar uma tabela
def create_table():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS estudantes (
            NAME VARCHAR(20) NOT NULL,
            BRANCH VARCHAR(50),
            ROLL INT NOT NULL,
            SECTION VARCHAR(5),
            AGE INT
        )
        """
        cursor.execute(create_table_query)
        connection.commit()
        close_connection(connection)

# Função para inserir um único registro
def insert_single_record():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "INSERT INTO estudantes (NAME, BRANCH, ROLL, SECTION, AGE) VALUES (%s, %s, %s, %s, %s)"
        val = ("Ram", "CSE", 85, "B", 19)
        cursor.execute(sql, val)
        connection.commit()
        close_connection(connection)

# Função para inserir múltiplos registros
def insert_multiple_records():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "INSERT INTO estudantes (NAME, BRANCH, ROLL, SECTION, AGE) VALUES (%s, %s, %s, %s, %s)"
        val = [
            ("Nikhil", "CSE", 98, "A", 18),
            ("Nisha", "CSE", 99, "A", 18),
            ("Rohan", "MAE", 43, "B", 20),
            ("Amit", "ECE", 24, "A", 21),
            ("Anil", "MAE", 45, "B", 20),
            ("Megha", "ECE", 55, "A", 22),
            ("Sita", "CSE", 95, "A", 19)
        ]
        cursor.executemany(sql, val)
        connection.commit()
        close_connection(connection)

# Função para buscar dados
def fetch_data():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "SELECT NAME, ROLL FROM estudantes"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
        close_connection(connection)

# Função para buscar dados com filtro
def fetch_data_with_condition():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM estudantes WHERE AGE >= 20"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
        close_connection(connection)

# Função para atualizar dados
def update_data():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE estudantes SET AGE = 23 WHERE NAME = 'Ram'"
        cursor.execute(query)
        connection.commit()
        close_connection(connection)

# Função para deletar dados
def delete_data():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM estudantes WHERE NAME = 'Ram'"
        cursor.execute(query)
        connection.commit()
        close_connection(connection)

# Função para deletar tabela
def drop_table():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "DROP TABLE IF EXISTS estudantes"
        cursor.execute(query)
        connection.commit()
        close_connection(connection)

# Função principal para executar as operações desejadas
def main():
     create_table()
    # insert_single_record()
    # insert_multiple_records()
    # fetch_data()
    # fetch_data_with_condition()
    # update_data()
    # delete_data()
    # drop_table()

if __name__ == "__main__":
    main()
