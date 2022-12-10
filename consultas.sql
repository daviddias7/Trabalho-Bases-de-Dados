-- A consulta abaixo eh relativa a obter todos os gastos de um gato especifico
-- e mostrar o valor do gasto, a nota fiscal e qual membro realizou o pagamento
select g.nota_fiscal, g.valor_do_gasto, p.nome
from gastos g, pessoa p, gato_resgatado gr
where (gr.nome LIKE 'NOME_DO_GATO' and gr.abrigo = g.nota_fiscal and g.membro_pagamento = p.cpf);


--selecionar veterinarios que ja atenderam todos os gatos
select * from Veterinario v 
Where not exists (
 Select * from veterinario v
 Minus
 (Select atributos de veterinario aq from veterinario v join gato g
   On v.gato <> g.nome)
);

--numero de doações recebidas e valor acumulado por membro
SELECT D.CPF_MEMBRO, COUNT(D.DATAHORA) AS NUMERO_DE_DOACOES, SUM(QUANTIA) AS QUANTIA_RECEBIDA FROM  
DOACAO D LEFT JOIN MEMBRO M ON D.CPF_MEMBRO= M.CPF
GROUP BY D.CPF_MEMBRO;

-- Quantidade de gatos livres avistados por pessoa
SELECT P.CPF , COUNT(G.NOME) AS GATOS_AVISTADOS  FROM
PESSOA P  JOIN AVISTAMENTO A ON P.CPF= A.PESSOA
JOIN RELACIONA R ON A.DATAHORA=R.AVISTAMENTO 
JOIN GATO_LIVRE G ON R.GATO= G.NOME
GROUP BY P.CPF;
