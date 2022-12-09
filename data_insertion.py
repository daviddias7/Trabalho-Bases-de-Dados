import re
import cx_Oracle

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
                    return "NULL"
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
            else:
                if(self.applyUpper): value = value.upper()
                if(self.value_is_possible(value)):
                    if(self.regex != ""):
                        check = re.search(self.regex, value)
                        if not check:
                            print("O valor digitado nao esta no padrao especificado")
                            continue
                    return value
                else:
                    self.print_possible_values()
                    continue



class Table:

    def __init__(self):
        self.atributes = []

    def insert_data(self):
        atribute_values = []
        for atribute in self.atributes:
            atribute_values.append(atribute.get_value())

        return atribute_values


class Pessoa(Table):

    def __init__(self):
        super().__init__()
        self.atributes = [
                Atribute("CPF", False, "string", "[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}", [], False),
                Atribute("NOME", False, "string", "^[a-zA-Z ]{1,20}$", [], True)
                ]
    def insert_data(self, connection):
        sql = """INSERT INTO PESSOA (CPF, NOME)
          VALUES (:P_CPF, :P_NOME)"""

        cursor = connection.cursor()

        while(True):
            data = super().insert_data()
            print("Tentando inserir o registro " + str(data) + " na tabela Pessoa")

            try:
                cursor.execute(sql, data)
                connection.commit()
                print("Sucesso ao inserir o registro!")
                return
            except cx_Oracle.DatabaseError as e:
                print("Um erro ocorreu na tentativa de se inserir o registro: ", e.args[0].message)
                print("Por favor, verifique o erro e insira os dados novamente.")


class Membro(Table):

    def __init__(self):
        super().__init__()
        self.atributes = [
                Atribute("CPF", False, "string", "[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}", [], False),
                Atribute("FUNCAO", False, "string", "", ['FINANCEIRO', 'MARKETING'], True)
                ]

class Doador(Table):

    def __init__(self):
        super().__init__()
        self.atributes = [
                Atribute("CPF", False, "string", "[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}", [], False),
                ]

class Adotante(Table):

    def __init__(self):
        super().__init__()
        self.atributes = [
                Atribute("CPF", False, "string", "[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}", [], False),
                Atribute("RUA", True, "string", "^[a-zA-Z ]{1,50}$", [], True),
                Atribute("NUMERO", True, "int", "", [], False),
                Atribute("BAIRRO", True, "string", "^[a-zA-Z ]{1,50}$", [], True),
                Atribute("CIDADE", True, "string", "^[a-zA-Z ]{1,30}$", [], True)
                ]

class Gastos(Table):

    def __init__(self):
        super().__init__()
        self.atributes = [
                Atribute("NOTA_FISCAL", False, "string", "[0-9]{9}", [], False),
                Atribute("ORIGEM", False, "string", "^[a-zA-Z ]{1,16}$", [], True),
                Atribute("VALOR_DO_GASTO", False, "float", "", [], False),
                Atribute("MEMBRO_PAGAMENTO", True, "string", "[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}", [], False),
                Atribute("FUNCAO", True, "string", "", ["FINANCEIRO", "MARKETING"], True)
                ]

tables = [("PESSOA", Pessoa()),
        ("MEMBRO", Membro()),
        ("DOADOR", Doador()),
        ("ADOTANTE", Adotante()),
        ("GASTOS", Gastos()),
        ("ABRIGO_TEMPORARIO", Pessoa()),
        ("GATO", Pessoa()),
        ("GATO_ADOTADO", Pessoa()),
        ("GATO_RESGATADO", Pessoa()),
        ("GATO_LIVRE", Pessoa()),
        ("VETERINARIO", Pessoa()),
        ("DOACAO", Pessoa()),
        ("AVISTAMENTO", Pessoa()),
        ("RELACIONA", Pessoa())]

