import cx_Oracle
import config
import user_interaction

con = None

user_interaction.application_title()

try:

    #con = cx_Oracle.connect(config.username, config.password, config.dsn, encoding=config.encoding)

    print("Conexao com o banco de dados estabelecida.")

    opt = user_interaction.option_selection()



except cx_Oracle.DatabaseError as e:
    print("Ocorreu um problema ao se conectar com o banco de dados: ", e)




