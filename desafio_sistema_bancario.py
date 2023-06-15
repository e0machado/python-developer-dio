menu = """
========== SISTEMA BANCÁRIO - DESAFIO PYTHON - DIO ==========

Digite a opção desejada:

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=============================================================

=> """

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_QTDE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.upper() == "D":
        valor_deposito = float(input("Digite o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Deposito no valor de R$ {valor_deposito:.2f} realizado com sucesso!\n\n")

        else:
            print("Valor de depósito inválido, digite um valor válido!")
    
    elif opcao.upper() == "S":
        valor_saque = float(input("Digite o valor do saque: "))

        erro_saldo = valor_saque > saldo

        erro_limite = valor_saque > limite_saque

        erro_saques = numero_saques >= LIMITE_QTDE_SAQUES

        if erro_saldo:
            print("Saldo insuficiente, saque não efetuado!")

        elif erro_limite:
            print(f"Limite excedido, saque não efetuado! Seu limite por saque é de R$ {limite_saque:.2f}")

        elif erro_saques:
            print("Limite de saques diário atingido, saque não efetuado!\n")
            print(f"Seu limite de saques diários é de {LIMITE_QTDE_SAQUES} saques!")

        elif valor_deposito > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"Saque no valor de R$ {valor_saque:.2f} realizado com sucesso!\n\n")

        else:
            print("Valor de saque inválido, digite um valor válido!")

    elif opcao.upper() == "E":
        print("\n========================== EXTRATO ==========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================================")

    elif opcao.upper() == "Q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

print("Obrigado por utilizar o nosso sistema!")
