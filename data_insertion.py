import re
import cx_Oracle
import regex_checks
from datetime import datetime

class Atribute:
    def __init__(self, name, isNullable, pType, regex, possible_values, applyUpper):
        self.name = name
        self.isNullable = isNullable
        self.pType = pType
        self.regex = regex
        self.possible_values = possible_values
        self.applyUpper = applyUpper

    def print_possible_values(self):
        print("O valor digitado precisa estar entre: [ ", end="")

        for val in self.possible_values:
            print(str(val) + " ", end="")

        print("]")


    def value_is_possible(self, value):
        if(len(self.possible_values) == 0): return True

        return (value in self.possible_values)

    def get_value(self):

        while(True):
            value = input("Insira o valor de " + self.name + ": ")

            if(value == ""):
                if(self.isNullable):
                    return None
                else:
                    print(self.name + " nao pode ser um valor nulo.")
                    continue

            if(self.pType == "int"):
                if(not value.isdigit()):
                    print("O valor digitado precisa ser um numero inteiro.")
                    continue
                else:
                    ivalue = int(value)
                    if(self.value_is_possible(ivalue)): return ivalue
                    else:
                        self.print_possible_values()
                        continue
            elif(self.pType == "float"):
                value.replace(',', '.')

                try:
                    fvalue = float(value)
                    if(self.value_is_possible(fvalue)): return fvalue
                    else:
                        self.print_possible_values()
                        continue
                except:
                    print("O valor digitado precisa ser um numero real")
                    continue
            elif(self.pType == "string"):
                if(self.applyUpper): value = value.upper()
                if(self.value_is_possible(value)):
                    if(self.regex[0] != ""):
                        check = re.search(self.regex[0], value)
                        if not check:
                            print("O valor digitado precisa " + self.regex[1])
                            continue
                    return value
                else:
                    self.print_possible_values()
                    continue
            elif(self.pType == "date"):
                check = re.search(self.regex[0], value)
                if not check:
                    print("O valor digitado precisa " + self.regex[1])
                    continue

                return datetime.strptime(value, "%Y/%m/%d %H:%M:%S")






class Table:

    def __init__(self, atributes, sql_insert, table_name):
        self.atributes = atributes
        self.sql_insert = sql_insert
        self.table_name = table_name

    def insert_data(self, connection):
        cursor = connection.cursor()

        while(True):
            atribute_values = []
            for atribute in self.atributes:
                atribute_values.append(atribute.get_value())
            print("Tentando inserir o registro " + str(atribute_values) + " na tabela " + self.table_name)

            try:
                cursor.execute(self.sql_insert, atribute_values)
                connection.commit()
                print("Sucesso ao inserir o registro!")
                return
            except cx_Oracle.DatabaseError as e:
                print("Um erro ocorreu na tentativa de se inserir o registro: ", e.args[0].message)
                print("Por favor, verifique o erro e insira os dados novamente.")


class Pessoa(Table):

    def __init__(self):
        atributes = [
                Atribute("CPF", False, "string", regex_checks.cpf, [], False),
                Atribute("NOME", False, "string", regex_checks.max_string(20), [], True)
                ]
        sql_insert = """INSERT INTO PESSOA (CPF, NOME)
          VALUES (:P_CPF, :P_NOME)"""

        table_name = "PESSOA"

        super().__init__(atributes, sql_insert, table_name)


class Membro(Table):

    def __init__(self):
        atributes = [
                Atribute("CPF", False, "string", regex_checks.cpf, [], False),
                Atribute("FUNCAO", False, "string", regex_checks.empty, ['FINANCEIRO', 'MARKETING'], True)
                ]

        sql_insert = """INSERT INTO MEMBRO (CPF, FUNCAO)
          VALUES (:M_CPF, :M_FUNCAO)"""

        table_name = "MEMBRO"

        super().__init__(atributes, sql_insert, table_name)

class Doador(Table):

    def __init__(self):
        atributes = [
                Atribute("CPF", False, "string", regex_checks.cpf, [], False),
                ]

        sql_insert = """INSERT INTO DOADOR (CPF)
          VALUES (:D_CPF)"""

        table_name = "DOADOR"

        super().__init__(atributes, sql_insert, table_name)

class Adotante(Table):

    def __init__(self):
        atributes = [
                Atribute("CPF", False, "string", regex_checks.cpf, [], False),
                Atribute("RUA", True, "string", regex_checks.max_string(50), [], True),
                Atribute("NUMERO", True, "int", "", [], False),
                Atribute("BAIRRO", True, "string", regex_checks.max_string(50), [], True),
                Atribute("CIDADE", True, "string", regex_checks.max_string(30), [], True)
                ]

        sql_insert = """INSERT INTO DOADOR (CPF, RUA, NUMERO, BAIRRO, CIDADE)
          VALUES (:A_CPF, :A_RUA, :A_NUMERO, :A_BAIRRO, :A_CIDADE)"""

        table_name = "ADOTANTE"

        super().__init__(atributes, sql_insert, table_name)

class Gastos(Table):

    def __init__(self):
        atributes = [
                Atribute("NOTA_FISCAL", False, "string", regex_checks.max_number(9), [], False),
                Atribute("ORIGEM", False, "string", regex_checks.max_string(16), [], True),
                Atribute("VALOR_DO_GASTO", False, "float", "", [], False),
                Atribute("MEMBRO_PAGAMENTO", True, "string", regex_checks.cpf, [], False),
                Atribute("FUNCAO", True, "string", "", ["FINANCEIRO", "MARKETING"], True)
                ]

        sql_insert = """INSERT INTO GASTOS (NOTA_FISCAL, ORIGEM, VALOR_DO_GASTO, MEMBRO_PAGAMENTO)
          VALUES (:G_NOTA_FISCAL, :G_ORIGEM, :G_VALOR_DO_GASTO, :G_MEMBRO_PAGAMENTO)"""

        table_name = "GASTOS"

        super().__init__(atributes, sql_insert, table_name)

class AbrigoTemporario(Table):

    def __init__(self):
        atributes = [
                Atribute("NOTA_FISCAL", False, "string", regex_checks.max_number(9), [], False),
                Atribute("RUA", False, "string", regex_checks.max_string(50), [], True),
                Atribute("NUMERO", False, "int", "", [], False),
                ]

        sql_insert = """INSERT INTO ABRIGO_TEMPORARIO (NOTA_FISCAL, RUA, NUMERO)
          VALUES (:A_NOTA_FISCAL, :A_ORIGEM, :A_VALOR_DO_GASTO)"""

        table_name = "ABRIGO_TEMPORARIO"

        super().__init__(atributes, sql_insert, table_name)

class Gato(Table):

    def __init__(self):
        atributes = [
                Atribute("NOME", False, "string", regex_checks.max_string(20), [], True),
                Atribute("RACA", True, "string", regex_checks.max_string(20), [], True),
                Atribute("CONDICAO", False, "string", regex_checks.max_string(10), ["RESGATADO", "ADOTADO", "LIVRE"], True),
                Atribute("MEMBRO_ANUNCIANTE", True, "string", regex_checks.cpf, [], False),
                Atribute("FUNCAO", True, "string", regex_checks.max_string(10), ["FINANCEIRO", "MARKETING"], True),
                ]

        sql_insert = """INSERT INTO GATO (NOME, RACA, CONDICAO, MEMBRO_ANUNCIANTE, FUNCAO)
          VALUES (:G_NOME, :G_RACA, :G_CONDICAO, :G_MEMBRO_ANUNCIANTE, :G_FUNCAO)"""

        table_name = "GATO"

        super().__init__(atributes, sql_insert, table_name)

class GatoAdotado(Table):

    def __init__(self):
        atributes = [
                Atribute("NOME", False, "string", regex_checks.max_string(20), [], True),
                Atribute("ADOTANTE", False, "string", regex_checks.cpf, [], False)
                ]

        sql_insert = """INSERT INTO GATO_ADOTADO (NOME, ADOTANTE)
          VALUES (:G_NOME, :G_ADOTANTE)"""

        table_name = "GATO_ADOTADO"

        super().__init__(atributes, sql_insert, table_name)

class GatoResgatado(Table):

    def __init__(self):
        atributes = [
                Atribute("NOME", False, "string", regex_checks.max_string(20), [], True),
                Atribute("CASTRADO", False, "string", regex_checks.empty, ["Y", "N"], True),
                Atribute("ABRIGO", False, "string", regex_checks.max_number(9), [], False)
                ]

        sql_insert = """INSERT INTO GATO_RESGATADO (NOME, CASTRADO, ABRIGO)
          VALUES (:G_NOME, :G_CASTRADO, :G_ABRIGO)"""

        table_name = "GATO_RESGATADO"

        super().__init__(atributes, sql_insert, table_name)

class GatoLivre(Table):

    def __init__(self):
        atributes = [
                Atribute("NOME", False, "string", regex_checks.max_string(20), [], True),
                ]

        sql_insert = """INSERT INTO GATO_LIVRE (NOME)
          VALUES (:G_NOME)"""

        table_name = "GATO_LIVRE"

        super().__init__(atributes, sql_insert, table_name)

class Veterinario(Table):

    def __init__(self):
        atributes = [
                Atribute("NOTA_FISCAL", False, "string", regex_checks.max_number(9), [], False),
                Atribute("CRMV", True, "string", regex_checks.max_number(9), [], False),
                Atribute("NOME", True, "string", regex_checks.max_string(20), [], True),
                Atribute("GATO", False, "string", regex_checks.max_string(20), [], True),
                ]

        sql_insert = """INSERT INTO VETERINARIO (NOTA_FISCAL, CRMV, NOME, GATO)
          VALUES (:V_NOTA_FISCAL, :V_CRMV, :V_NOME, :V_GATO)"""

        table_name = "VETERINARIO"

        super().__init__(atributes, sql_insert, table_name)

class Doacao(Table):

    def __init__(self):
        atributes = [
                Atribute("DATAHORA", False, "date", regex_checks.date, [], False),
                Atribute("CPF_MEMBRO", False, "string", regex_checks.cpf, [], False),
                Atribute("FUNCAO_MEMBRO", False, "string", regex_checks.empty, ["FINANCEIRO"], True),
                Atribute("CPF_DOADOR", False, "string", regex_checks.cpf, [], False),
                Atribute("QUANTIA", False, "float", regex_checks.empty, [], False)
                ]

        sql_insert = """INSERT INTO DOACAO (DATAHORA, CPF_MEMBRO, FUNCAO_MEMBRO, CPF_DOADOR, QUANTIA)
          VALUES (:D_DOACAO, :D_CPF_MEMBRO, :D_FUNCAO_MEMBRO, :D_CPF_DOADOR, :D_QUANTIA)"""

        table_name = "DOACAO"

        super().__init__(atributes, sql_insert, table_name)

class Avistamento(Table):

    def __init__(self):
        atributes = [
                Atribute("DATAHORA", False, "date", regex_checks.date, [], False),
                Atribute("DESCRICAO_DO_LOCAL", False, "string", regex_checks.max_string(100), [], False),
                Atribute("PESSOA", True, "string", regex_checks.cpf, [], False)
                ]

        sql_insert = """INSERT INTO AVISTAMENTO (DATAHORA, DESCRICAO_DO_LOCAL, PESSOA)
          VALUES (:A_DATAHORA, :A_DESCRICAO_DO_LOCAL, :A_PESSOA)"""

        table_name = "AVISTAMENTO"

        super().__init__(atributes, sql_insert, table_name)

class Relaciona(Table):
    def __init__(self):
        atributes = [
                Atribute("GATO", False, "string", regex_checks.empty, [], True),
                Atribute("AVISTAMENTO", False, "date", regex_checks.date, [], False),
                Atribute("MEMBRO", False, "string", regex_checks.cpf, [], False),
                Atribute("FUNCAO", False, "string", regex_checks.empty, ["FINANCEIRO", "MARKETING"], True),
                ]

        sql_insert = """INSERT INTO RELACIONA (GATO, AVISTAMENTO, MEMBRO, FUNCAO)
          VALUES (:R_GATO, :R_AVISTAMENTO, :R_MEMBRO, :R_FUNCAO)"""

        table_name = "RELACIONA"

        super().__init__(atributes, sql_insert, table_name)

tables = [("PESSOA", Pessoa()),
        ("MEMBRO", Membro()),
        ("DOADOR", Doador()),
        ("ADOTANTE", Adotante()),
        ("GASTOS", Gastos()),
        ("ABRIGO_TEMPORARIO", AbrigoTemporario()),
        ("GATO", Gato()),
        ("GATO_ADOTADO", GatoAdotado()),
        ("GATO_RESGATADO", GatoResgatado()),
        ("GATO_LIVRE", GatoLivre()),
        ("VETERINARIO", Veterinario()),
        ("DOACAO", Doacao()),
        ("AVISTAMENTO", Avistamento()),
        ("RELACIONA", Relaciona())]

