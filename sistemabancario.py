import textwrap

menu = """
_____ Sistema Bancário _____

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo cliente
[5] Nova conta
[6] Listar contas
[7] Sair

=> """

LIMITE_SAQUES_CONTA = 3
AGENCIA = "0001"

saldo_conta = 0
limite_diario = 500
extrato_conta = ""
nro_saques_conta = 0
clientes = []
contas_banco = []

def depositar(saldo, extrato, /):
    valor_deposito = float(input("Valor do Depósito: "))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ \t{valor_deposito:.2f}\n"
        print(f"Depósito: R$ {valor_deposito:.2f} realizado!")
    else:
        print("Valor incorreto para depósito!")
    return saldo, extrato

def sacar(*, valor, saldo, extrato, limite, numero_saques, limite_saques ):

    if valor > saldo:
        print("Falha na operação! Não tem saldo.")

    elif valor > limite:
        print("Falha na operação! Saque excedeu o limite diário.") 

    elif numero_saques >= limite_saques:
        print ("Falha na operação! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ \t{valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado!")     
            
    else:
        print("Falha na Operação! Valor inválido.")
    return saldo, extrato, numero_saques

def extrato(saldo, /,*, extrato):
    print("\n____________Extrato da Conta____________")
    print("Sem movimentações na conta" if not extrato else extrato)
    print(f"Saldo R$:\t{saldo:.2f}")
    print("________________________________________")   

def novo_cliente(clientes):


    cpf = input("Digite somente os números do CPF: ")
    cliente = filtro(cpf, clientes)

    if cliente:
        print("Cliente já cadastrado!")
        return
    
    nome = input("Nome completo: ")
    nascimento = input ("Data de nascimento: ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla do estado): ")
    clientes.append({"nome":nome, "cpf":cpf, "nascimento":nascimento, "endereco":endereco})
    print("Cliente cadastrado!")

def nova_conta(AGENCIA, clientes, contas_banco):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtro(cpf, clientes)

    if cliente:
        print("Conta criada!")
        return {"agencia": AGENCIA, "cliente": cliente, "numero_conta": contas_banco}   

    print("Cliente não cadastrado!") 

def filtro(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
        """
        print("_" * 60)
        print(textwrap.dedent(linha))

while True:

    opcao_menu = int(input(menu))

    if opcao_menu == 1:
        saldo_conta, extrato_conta = depositar(saldo_conta, extrato_conta)

    elif opcao_menu == 2:
        valor_saque = float(input("Valor do Saque: "))

        saldo_conta, extrato_conta, nro_saques_conta = sacar(
            valor = valor_saque,
            saldo = saldo_conta,
            extrato = extrato_conta,
            limite = limite_diario,
            numero_saques = nro_saques_conta,
            limite_saques = LIMITE_SAQUES_CONTA
        )
    
    elif opcao_menu == 3:
        extrato(saldo_conta, extrato = extrato_conta)        

    elif opcao_menu == 4:
        novo_cliente(clientes)

    elif opcao_menu == 5:
        numero_conta = len(contas_banco) + 1
        conta = nova_conta(AGENCIA, clientes, numero_conta)
        
        if conta:
           contas_banco.append(conta)
    
    elif opcao_menu == 6:
        listar_contas(contas_banco)

    elif opcao_menu == 7:
        break

    else:
        print("Operação selecionada inválida!!!")


