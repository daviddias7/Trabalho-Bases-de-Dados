import cx_Oracle
import config
import user_interaction as ui

con = None

ui.application_title()

try:

    #con = cx_Oracle.connect(config.username, config.password, config.dsn, encoding=config.encoding)

    print("Conexao com o banco de dados estabelecida.")

    opt = ui.option_selection()

    if(opt == 1):
        table = ui.table_selection()
    elif(opt == 2):
        print("Obrigato por usar o Gatos do C2!")



except cx_Oracle.DatabaseError as e:
    print("Ocorreu um problema ao se conectar com o banco de dados: ", e)




