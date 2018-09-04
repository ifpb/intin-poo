from Pedido import Pedido
from ItemPedido import ItemPedido
from Produto import Produto

motog = Produto(1234, 500.00, "Moto G")
galaxy  = Produto(1234, 700.00, "Samsung Galaxy")
zenphone = Produto(1234, 400.00, "Zen Phone")
iphone = Produto(3213, 4000.00, "IPhone X")

p1 = Pedido()
item = ItemPedido(motog,3)
p1.adicionar_item(item)
item = ItemPedido(galaxy,2)
p1.adicionar_item(item)
item = ItemPedido(zenphone,2)
p1.adicionar_item(item)
print("Valor total do pedido 1 = ", p1.obter_total())

p2 = Pedido()
item = ItemPedido(iphone, 1)
p2.adicionar_item(item)
print("Valor total do pedido 2 = ", p2.obter_total())