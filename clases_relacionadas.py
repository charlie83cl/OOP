class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.cuenta = cuentaBancaria(interes=0.02, balance=0)

    def deposito(self, monto):
            self.cuenta.deposito(monto)
            return self

    def retiro(self, monto):
            self.cuenta.retiro(monto)
            return self

    def showmeThemoney(self):
            return f"Saldito: ${self.nombre}, saldo: ${self.cuenta.showmeThemoney()}"

    def transferencia(self,other_user,monto):
            self.retiro(monto)
            other_user.deposito(monto)



class cuentaBancaria:
    def __init__(self, interes = 0.01, balance = 0):
        self.interes = interes
        self.balance = balance

    def deposito(self, monto):
        self.balance += monto                           
        return self

    def retiro(self, monto):
        if self.balance >= monto:
            self.balance -= monto
        else:
            print("No tienes Saldo: y el costo por operacion es $5 pesos")
            self.balance -= 5
        return self

    def showmeThemoney(self):
        return f"Saldito: ${self.balance}"

    def interesOperatorio(self):
        if self.balance > 0:
            self.balance += self.balance * self.insteres
        return self



usuario1 = Usuario("Esteban","email@email.com")
usuario2 = Usuario("Aquiles","baeza@ailalo.cl")
usuario3 = Usuario("Elba","lazo@propi.org")

usuario1.transferencia(usuario2, 15000)

print(usuario1.showmeThemoney())
print(usuario2.showmeThemoney())
print(usuario3.showmeThemoney())
