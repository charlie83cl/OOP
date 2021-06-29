from store import Store
from product import Product

producto1 = Product(1001,"te negro",1000,"Infusion")
producto2 = Product(1002,"cafe",1500,"Infusion")
producto3 = Product(1003,"choclate",3000,"Alimento")
producto4 = Product(1004,"mate", 1000, "Alimento")
producto5 = Product(1005,"paltas", 15000, "Bebestible")

tienda1 = Store("Donde Jose")
tienda1.add_product(producto1)
tienda1.add_product(producto2)
tienda1.add_product(producto3)
tienda1.add_product(producto4)
tienda1.add_product(producto5)

print(f"Listado de Productos de la tienda {tienda1.name}")
for i in tienda1.products:
    print(i.print_info())

print("*"*50)
print("Vendiendo un producto...")
tienda1.sell_product(1002)

print("*"*50)
print("Listado de productos que quedan disponibles")
for i in tienda1.products:
    print(i.print_info())

print("*"*50)
print("Actualizaremos el precio de todos los productos en 20%")
tienda1.inflation(20)
print("Listado de productos con precios actualizados")
for i in tienda1.products:
    print(i.print_info())

print("*"*50)
print("Actualizaremos el precio de todos los alimento entregando un descuento del 40%")
tienda1.set_clearance("Alimento", 40)
print("Listado de productos con precios actualizados")
for i in tienda1.products:
    print(i.print_info())






