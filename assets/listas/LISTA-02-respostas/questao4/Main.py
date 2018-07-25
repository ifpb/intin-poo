from CartaoMensagem import CartaoMensagem
from MensagemAniversario import MensagemAniversario
from MensagemDiaDosNamorados import MensagemDiaDosNamorados
from MensagemNatal import MensagemNatal

msgs = []
msg1 = MensagemAniversario("Murilo")
msgs.append(msg1)
msgs.append(MensagemAniversario("Marina"))
msgs.append(MensagemDiaDosNamorados("Nina"))
msgs.append(MensagemNatal("Nina"))

for msg in msgs:
    print(msg.retornar_mensagem("Diego"))