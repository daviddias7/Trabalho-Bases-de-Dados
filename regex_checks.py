cpf = ("[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}", "possuir o formato xxx.xxx.xxx-xx")

empty = ("", "")

date = ("[0-9]{4}\/[0-9]{2}\/[0-9]{2}\ [0-9]{2}\:[0-9]{2}\:[0-9]{2}", "estar no formato YYYY/MM/DD HH24:MI:SS")

def max_number(max_len):
    max_len = str(max_len)
    return ("[0-9]{" + max_len + "}", "conter um numero de no maximo " + max_len)

def max_string(max_len):
    max_len = str(max_len)
    return ("^[a-zA-Z ]{1," + max_len + "}$", "conter no maximo " + max_len + " caracteres do alfabeto")
