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

cuenta1 = cuentaBancaria()
cuenta2 = cuentaBancaria(0.03, 2000)
cuenta3 = cuentaBancaria(1000)


print(cuenta1.deposito(500))