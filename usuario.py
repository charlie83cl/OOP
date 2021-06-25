class Usuario:
    def __init__(self,rut,nombre,email,pais):
        self.rut = rut
        self.nombre = nombre
        self.email = email
        self.pais = pais
        self.cuentarut = 0
    
    def info_usuario(self):
        reporte = '**************************************************\n'
        reporte +='Rut\t:' + self.rut + '\nNombre\t:' + self.nombre + '\nCorreo\t:' + self.email + '\nPais\t:' + self.pais + '\nSaldo\t:' + str(self.cuentarut) + '\n**************************************************'
        return reporte
    
    def deposito(self,monto):
        self.cuentarut += monto
    
    def retiro(self,monto): #la cantidad que se agregue al usuario1.retiro(1582135456) sera descontado del saldo en la cuenta
        self.cuentarut -= monto
        
    def saldo(self):    #
        saldito = 'Usuario: ' + self.nombre + ' su nuevo saldo es\t: $'+ str(self.cuentarut)
        saldito +='\n**************************************************\n'
        return saldito
    
    def transferencia(self,other_user,monto):
        self.retiro(monto)
        other_user.deposito(monto)

usuario1 = Usuario("15.000.000-1","Esteban","email@email.com","Chile")
usuario2 = Usuario("10.000.000-2","Aquiles","baeza@ailalo.cl","Peru")
usuario3 = Usuario("9.000.000-3","Elba","lazo@propi.org","Afganistan")

usuario1.deposito(300)
usuario1.deposito(300)
usuario1.deposito(300)
usuario1.retiro(500)
usuario1.saldo()

usuario2.deposito(1000)
usuario2.deposito(1000)
usuario2.retiro(500)
usuario2.retiro(500)
usuario2.saldo()

usuario3.deposito(1500)
usuario3.retiro(250)
usuario3.retiro(250)
usuario3.retiro(500)
usuario3.saldo()

#print(f"**************************************************\ntu rut es:{usuario1.rut}\nel usuario:{usuario1.nombre}\ncon correo:{usuario1.email}\nPais:{usuario1.pais}\nSaldo:${usuario1.cuentarut} Pesos")
print(usuario1.info_usuario())
print(usuario1.saldo())
print(usuario2.info_usuario())
print(usuario2.saldo())
print(usuario3.info_usuario())
print(usuario3.saldo())

usuario1.transferencia(usuario3, 14500)
print(usuario1.saldo())
print(usuario3.saldo())
