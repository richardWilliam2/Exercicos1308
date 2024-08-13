for i in range (3):
    #nome = input("your name: ")
    email = input("your e-mail: ")
    senha = input("your senha: ")
    if (email == "Richard" and senha == "1234"):
        print("Acesso permitido")
        opcao = input("1-saque 2-deposito 3-PIX")
        match opcao:
            case 1:
                saque = input ("Informe o valor do saque: ")
            case 2:
                dep = input ("Informe o calor do saque: ")
            case 3:
                pix = input ("informe o valor do saque: ")
            case 4:
                CC = input("Informe o valor do saque: ")
            case 5:
                Poupança= input("informe o valor do saque: ")

else:
    print("Acesso negado!!!")