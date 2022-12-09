# Esse arquivo contem o codigo inicial para criacao do esquema do banco
# juntamente com as insecoes base. Nao foram implementados os tratamentos
# de erros, assim como a aplicacao em si, pois nao se julgou necessario

import cx_Oracle
import config

con = cx_Oracle.connect(config.username, config.password, config.dsn, encoding=config.encoding)

#print(con)

cursor = con.cursor()
cursor.execute('SELECT * FROM PESSOA')
print(cursor.fetchall()[1])

#cursor.execute("DROP TABLE RELACIONA")
#cursor.execute("DROP TABLE AVISTAMENTO")
#cursor.execute("DROP TABLE DOACAO")
#cursor.execute("DROP TABLE VETERINARIO")
#cursor.execute("DROP TABLE GATO_LIVRE")
#cursor.execute("DROP TABLE GATO_RESGATADO")
#cursor.execute("DROP TABLE GATO_ADOTADO")
#cursor.execute("DROP TABLE GATO")
#cursor.execute("DROP TABLE ADOTANTE")
#cursor.execute("DROP TABLE DOADOR")
#cursor.execute("DROP TABLE ABRIGO_TEMPORARIO")
#cursor.execute("DROP TABLE GASTOS")
#cursor.execute("DROP TABLE MEMBRO")
#cursor.execute("DROP TABLE PESSOA")


#with open("esquema.sql", "r") as file:
#    commands = file.read().split(";")
#    commands.pop()
#    for command in commands:
#        command = command[command.find('C'):]
#        print("Executando comando: ", command.split("\n")[0], " ...")
#        cursor.execute(command)

#with open("dados.sql", "r") as file:
#    data = file.read().split(";")
#    data.pop()

    #print(data[len(data) - 1])
    #cursor.execute(data[len(data) - 1])
#    for d in data:
#        d = d[d.find('I'):]
#        print("Executando comando: ", d)
#        cursor.execute(d)

#con.commit()
cursor.close()
con.close()
