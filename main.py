from usuario import Usuario

usuario1 = Usuario("15.000.000-1","Esteban","email@email.com","Chile")
usuario2 = Usuario("10.000.000-2","Aquiles","baeza@ailalo.cl","Peru")
usuario3 = Usuario("9.000.000-3","Elba","lazo@propi.org","Afganistan")


usuario1.deposito(23000000)
print(usuario1.info_usuario())
