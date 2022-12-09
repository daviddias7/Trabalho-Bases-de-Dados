import cx_Oracle
import config

con = None
print(r"""
 .d8888b.           888                               888                .d8888b.   .d8888b.
d88P  Y88b          888                               888               d88P  Y88b d88P  Y88b
888    888          888                               888               888    888        888
888         8888b.  888888 .d88b.  .d8888b        .d88888  .d88b.       888             .d88P
888  88888     "88b 888   d88""88b 88K           d88" 888 d88""88b      888         .od888P"
888    888 .d888888 888   888  888 "Y8888b.      888  888 888  888      888    888 d88P"
Y88b  d88P 888  888 Y88b. Y88..88P      X88      Y88b 888 Y88..88P      Y88b  d88P 888"
 "Y8888P88 "Y888888  "Y888 "Y88P"   88888P'       "Y88888  "Y88P"        "Y8888P"  888888888


 _      _
 |\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \,
|            \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'



        """)

try:

    #con = cx_Oracle.connect(config.username, config.password, config.dsn, encoding=config.encoding)

    print("Conexao com o banco de dados estabelecida.")


except cx_Oracle.DatabaseError as e:
    print("Ocorreu um problema ao se conectar com o banco de dados: ", e)




