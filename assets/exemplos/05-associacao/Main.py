from Pessoa import Pessoa
from Endereco import Endereco

pessoa = Pessoa("Diego", "123123123", 30)
endereco1 = Endereco("Rua X", 13, "Bairro X", "Cajazeiras", "Paraiba")
endereco2 = Endereco("Rua AAA", 1313, "Bairro Y", "João Pessoa", "Paraiba")
pessoa.adicionarEndereco(endereco1)
pessoa.adicionarEndereco(endereco2)
for endereco in pessoa.enderecos:
    print("rua = ",endereco.rua)