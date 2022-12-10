-- A consulta abaixo eh relativa a obter todos os gastos de um gato especifico
-- e mostrar o valor do gasto, a nota fiscal e qual membro realizou o pagamento
select g.nota_fiscal, g.valor_do_gasto, p.nome
from gastos g, pessoa p, gato_resgatado gr
where (gr.nome LIKE 'NOME_DO_GATO' and gr.abrigo = g.nota_fiscal and g.membro_pagamento = p.cpf)
