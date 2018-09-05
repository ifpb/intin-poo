arq = open('/tmp/lista.txt', 'w')
texto = """
Lista de Alunos
---
Adriel Higor Rodrigues Lins da Silva
Ana Beatriz Ferreira Lira
Aquilla Maria Almeida
Brena Ellen Feitoza Marques
"""
arq.write(texto)
arq.close()