# try:
#     a = int(input("Digite um numero"))
#     b = int(input("Digite um numero"))
#     print(a/b)
# except ZeroDivisionError:
#     print("Nao pode dividir por zero")
from Pessoa import Pessoa
from IdadeInvalida import IdadeInvalida

try:
    pessoa = Pessoa("Diego", -1)
except IdadeInvalida:
    print("A idade deverá ser maior do que zero e menor do que 100")


