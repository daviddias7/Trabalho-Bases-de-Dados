import cx_Oracle
import config
import user_interaction as ui
import data_select

con = None

ui.application_title()


try:

    con = cx_Oracle.connect(config.username, config.password, config.dsn, encoding=config.encoding)

    print("Conexao com o banco de dados estabelecida.")

    opt = ui.option_selection()

    if(opt == 1):
        table_obj = ui.table_selection()
        table_obj.insert_data(con)
    elif(opt == 2):
        name = ui.cat_name()
        data_select.get_cat_outgoing(name, con)
    elif(opt == 3):
        print("Obrigato por usar o Gatos do C2!")



except cx_Oracle.DatabaseError as e:
    print("Ocorreu um problema ao se conectar com o banco de dados: ", e)




