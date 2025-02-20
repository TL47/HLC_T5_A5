class CuentaBancaria():
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def depositar(self, cantidad):
        self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad
    
    def ver_saldo(self):
        return(f"El saldo de la cuenta es de {self.cantidad}€.")

cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(300)
print(cuenta.ver_saldo())