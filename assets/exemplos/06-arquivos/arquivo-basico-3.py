arq = open('/tmp/lista.txt', 'r')
texto = arq.read()
print(texto)
arq.close()