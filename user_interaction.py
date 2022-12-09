def application_title():
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

def option_selection():
    options = ["Insercao de dados",
            "Deixar a aplicacao"]

    print("\nSelecione qual funcionalidade a ser executada (digite o numero entre os colchetes):")

    for i in range(len(options)):
        print("[" + str(i + 1) + "] " + options[i])


    opt = int(input("Funcionalidade: "))

    while(opt <= 0 or opt > len(options)):
        print("O valor " + str(opt) + " nao corresponde a nenhuma funcionalidade. Por favor, digite novamente.")
        opt = int(input("Opcao: "))

    return opt


def table_selection():
    table_names = ["PESSOA",
            "MEMBRO",
            "DOADOR",
            "ADOTANTE",
            "GASTOS",
            "ABRIGO_TEMPORARIO",
            "GATO",
            "GATO_ADOTADO",
            "GATO_RESGATADO",
            "GATO_LIVRE",
            "VETERINARIO",
            "DOACAO",
            "AVISTAMENTO",
            "RELACIONA"]

    print("\nSelecione qual a tabela desejada (digite o numero entre os colchetes):")

    for i in range(len(table_names)):
        print("[" + str(i + 1) + "] " + table_names[i])


    table = int(input("Tabela: "))

    while(table <= 0 or table > len(table_names)):
        print("O valor " + str(table) + " nao corresponde a nenhuma tabela. Por favor, digite novamente.")
        table = int(input("Tabela: "))

    print("Voce selecionou a tabela " + table_names[table - 1])
    return table
