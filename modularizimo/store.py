from product import Product

class Store:

    def __init__(self, name, products = []):
        self.name = name
        self.products = products

    def add_product (self, new_product):
        self.products.append(new_product)
        return self

    def sell_product (self, id):
        for producto in self.products:
            if producto.id == id:
                print(producto.print_info())
                self.products.remove(producto)
            
        #print(self.products[id-1].print_info())
        #self.products.pop(id-1)
        return self

    def inflation(self, percent_increase):
        for producto in self.products:
            producto.update_price(percent_increase) 
        return self       

    def set_clearance (self, category, percent_discount):
        for producto in self.products:
            if producto.category == category:
                producto.update_price(percent_discount,False)
        return self


