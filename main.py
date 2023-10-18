from mysql.connector import (connection)

db_con = connection.MySQLConnection(host = "localhost", user = "root", password = "", database = "meu_teste")

cursor = db_con.cursor()

while(True):
    print("Escolha uma opção")
    print("1 - Cadastrar")
    print("2 - Visualizar")
    print("3 - Sair")
    op = str(input("Digite: "))
    if(op == "1"):
        nome = str(input("Digite seu nome: "))
        idade = int(input("Digite sua idade: "))

        cursor.execute(f"INSERT INTO usuarios (nome, idade) VALUES ('{nome}', {idade})")

        db_con.commit()

        print("Cadastrado com sucesso")
    elif(op == "2"):
        cursor.execute("SELECT * FROM usuarios")
        dados = cursor.fetchall()
        for data in dados:
            print(data)
    elif(op == "3"):
        break