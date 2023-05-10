from models.cliente import Cliente
from models.conta import Conta


fulano: Cliente = Cliente('fulano', 'fulano@gmail.com', '212.213.123-91', '02/09/1132')

contaF: Conta = Conta(fulano)

print(fulano, contaF)
