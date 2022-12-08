import cx_Oracle
import config

con = None
try:

    con = cx_Oracle.connect(config.username, config.password, config.dsn, encoding=config.encoding)

    print("Conexao com o banco de dados estabelecida.")

except cx_Oracle.DatabaseError as e:
    print("Ocorreu um problema ao se conectar com o banco de dados: ", e)


print(con)


