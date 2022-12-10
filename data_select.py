def get_cat_outgoing(cat_name, connection):
    sql_select = """select g.nota_fiscal, g.valor_do_gasto, p.nome
    from gastos g, pessoa p, gato_resgatado gr
    where (gr.nome LIKE :c_name and gr.abrigo = g.nota_fiscal and g.membro_pagamento = p.cpf)"""

    cursor = connection.cursor()
    cursor.execute(sql_select, cat_name)
    print(cursor.fetchall())
