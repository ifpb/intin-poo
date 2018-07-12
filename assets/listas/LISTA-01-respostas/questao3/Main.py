from Ingresso import Ingresso
from IngressoVIP import IngressoVIP

ingressoNormal = Ingresso(10)
ingressoVIP = IngressoVIP(10, 5)

print("Preço do ingresso normal: ", end='')
ingressoNormal.imprimirValor()

print("Preço do ingresso VIP: ", end='')
ingressoVIP.imprimirValor()
