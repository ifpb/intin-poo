from Funcionario import Funcionario
from Endereco import Endereco

endereco = Endereco("Rua x", 123, "Bairro Y", "Cajazeiras", "Paraiba", "Brasil")
funcionario = Funcionario("Wilbert", 20, endereco, 2000)
print(funcionario)