import cx_Oracle
import config

con = cx_Oracle.connect(config.username, config.password, config.dsn, encoding=config.encoding)

print(con)


