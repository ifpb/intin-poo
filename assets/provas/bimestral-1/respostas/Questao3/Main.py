from VeiculoImportado import VeiculoImportado
from VeiculoNacional import VeiculoNacional


continuar = "sim"
veiculos = []
while(continuar == "sim"):
    print("Bem-vindo ao programa de cadastro de veiculos")
    tipo = input("Digite o tipo do veiculo")
    cor = input("Digite a cor do veiculo")
    placa = input("Digite a placa do veiculo")
    portas = int(input("Digite a quantidade de portas do veiculo"))
    preco = float(input("Digite o preco do veiculo"))
    nacionalidade = int(input("Digite a nacionalidade do veiculo (1=Nacional, 2=Importado)"))
    veiculo = None
    if (nacionalidade == 1):
        veiculo = VeiculoNacional(tipo, cor, placa, portas, preco)
    elif(nacionalidade == 2):
        veiculo = VeiculoImportado(tipo, cor, placa, portas, preco)
    else:
        print("Nacionalidade do veículo inválida")
    veiculos.append(veiculo)

    continuar = input("Deseja continuar? (sim, nao)")

for veiculo in veiculos:
    print("Preço do",veiculo.tipo,"=",veiculo.preco)