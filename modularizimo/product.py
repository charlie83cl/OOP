class Product:

    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased = True):
        if is_increased == True:
            self.price += (self.price * percent_change/100)
        else:
            self.price -= (self.price * percent_change/100)
        return self

    def print_info (self):
        return f"ID: {self.id} | Nombre: {self.name } | Precio: ${self.price} | Categoria: {self.category}"


#Creamos un producto
#producto1 = Product("Pan", 1500, "Alimentos")
#print(producto1.print_info()) """
    
