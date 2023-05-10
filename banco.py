from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('=======================================')
    print('=============== ATM ===================')
    print('============ Inova Bank ===============')
    print('=======================================')

    print('selecione uma opção no menu: ')
    print('1 - Criar Conta ')
    print('2 - Efetuar Saque')
    print('3 - Efetuar Deposito')
    print('4 - Efetuar Transferência')
    print('5 - Listar Contas')
    print('6 - Sair do Sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(1)
        menu()


def criar_conta() -> None:
    print('informe os dados do cliente: ')

    nome: str = input('Nome do Cliente: ')
    email: str = input('E-mail do Cliente: ')
    cpf: str = input('CPF do Cliente: ')
    data_nascimento = input('Data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso.')
    print('Dados da conta: ')
    print('-----------------')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor o depósito: '))

            conta.depositar(valor)
        else:
            print(f'Não foi encontrada uma conta com número {numero}')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_origem: int = int(input('Informe o número da sua conta: '))

        conta_origem: Conta = buscar_conta_por_numero(numero_origem)

        if conta_origem:
            numero_destino: int = int(input(
                'Informe o número da conta destino: '))

            conta_destino: Conta = buscar_conta_por_numero(numero_destino)
            if conta_destino:
                valor: float = float(
                    input('Informe o valor da transferência: '))

                conta_origem.transferir(conta_destino, valor)
            else:
                print(f'A conta destino com número {numero_destino}\
                       não foi encontrada.')
        else:
            print(f'A sua conta com número {numero_origem}\
                   não foi encontrada.')

    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')

        for conta in contas:
            print(conta)
            print('--------------')
            sleep(1)
    else:
        print('Não existem contas cadastradas.')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
