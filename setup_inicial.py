# Esse arquivo contem o codigo inicial para criacao do esquema do banco
# juntamente com as insecoes base. Nao foram implementados os tratamentos
# de erros, assim como a aplicacao em si, pois nao se julgou necessario

import cx_Oracle
import config

con = cx_Oracle.connect(config.username, config.password, config.dsn, encoding=config.encoding)

print(con)

cursor = con.cursor()

with open("esquema.sql", "r") as file:
    commands = file.read().split(";")
    print(commands)
    commands.pop()
    for command in commands:
        command = command[command.find('C'):]
        print("Executando comando: ", command.split("\n")[0], " ...")
        cursor.execute(command)

