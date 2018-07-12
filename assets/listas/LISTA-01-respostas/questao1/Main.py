from Jogador import JogadorFutebol
import datetime

jogador = JogadorFutebol("Neymar", "atacante", datetime.date(1992, 2, 5), "brasileiro", 1.75, 70)
print(jogador)
print("Faltam %d anos para %s se aposentar" % (jogador.faltaPraAposentar(), jogador.nome))