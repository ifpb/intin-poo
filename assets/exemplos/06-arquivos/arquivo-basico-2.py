arq = open('/tmp/lista.txt', 'w')

lista = []
lista.append("Lista de Alunos\n")
lista.append("---\n")
lista.append("Adriel Higor Rodrigues Lins da Silva\n")
lista.append("Ana Beatriz Ferreira Lira\n")
lista.append("Aquilla Maria Almeida\n")
lista.append("Brena Ellen Feitoza Marques\n")
arq.writelines(lista)
arq.close()