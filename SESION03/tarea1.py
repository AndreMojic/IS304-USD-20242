'''
Tarea para antes de la  próxima clase:
Crear un programa en Python que cree una clase denominada CuentaBancaria. Agregar encapsulamiento y sobrecarga del constructor de clase, asi como los métodos get y set requeridos para gestionar los atributos de dicha clase.
Los atributos de la clase debern ser: __numeroCta, __nombreCliente, __fechaApertura, __saldo.
Agregar metodos para aperturar cuentas, realizar consignaciones y retiros controlados (es decir, no permitir consignaciones negativas, ni retiros superiores al saldo, las aperturas deben exigir un valor inicial mínimo de 100 mil pesos).
Crear un menú para crear objetos y realizar las diversas operaciones referidas.

'''
class CuentaBancaria:
  Andres Mojica
  Tarea 01

import datetime

class BancoCuenta:
    def __init__(self, cuenta_numero=None, cliente_nombre=None, apertura_fecha=None, balance=0.0):
        if cuenta_numero and cliente_nombre and apertura_fecha:
            self.__cuenta_numero = cuenta_numero
            self.__cliente_nombre = cliente_nombre
            self.__apertura_fecha = apertura_fecha
            self.__balance = balance
        else:
            self.__cuenta_numero = ""
            self.__cliente_nombre = ""
            self.__apertura_fecha = ""
            self.__balance = 0.0

    def obtener_cuenta_numero(self):
        return self.__cuenta_numero

    def obtener_cliente_nombre(self):
        return self.__cliente_nombre

    def obtener_apertura_fecha(self):
        return self.__apertura_fecha

    def obtener_balance(self):
        return self.__balance

    def establecer_cuenta_numero(self, cuenta_numero):
        self.__cuenta_numero = cuenta_numero

    def establecer_cliente_nombre(self, cliente_nombre):
        self.__cliente_nombre = cliente_nombre

    def establecer_apertura_fecha(self, apertura_fecha):
        self.__apertura_fecha = apertura_fecha

    def establecer_balance(self, balance):
        self.__balance = balance

    def iniciar_cuenta(self, cuenta_numero, cliente_nombre, balance_inicial):
        if balance_inicial < 100000:
            print("El balance inicial debe ser mayor a 100000 pesos")
            return False
        self.__cuenta_numero = cuenta_numero
        self.__cliente_nombre = cliente_nombre
        self.__balance = balance_inicial
        self.__apertura_fecha = datetime.date.today()
        print("Cliente registrado exitosamente")
        return True

    def hacer_consignacion(self, monto):
        if monto > 0:
            self.__balance += monto
            print(f"Consignación exitosa. Nuevo balance: {self.__balance}")
        else:
            print("El monto a consignar debe ser positivo")

    def hacer_retiro(self, monto):
        if 0 < monto <= self.__balance:
            self.__balance -= monto
            print(f"Retiro exitoso. Nuevo balance: {self.__balance}")
        else:
            print("Monto inválido para retiro")

    def mostrar_detalles(self):
        print(f"Número de cuenta: {self.__cuenta_numero}")
        print(f"Nombre del cliente: {self.__cliente_nombre}")
        print(f"Fecha de apertura: {self.__apertura_fecha}")
        print(f"Balance actual: {self.__balance}")

def mostrar_menu():
    print("\n --- ¡Bienvenido a tu Banco! ---")
    print("\n -- Menú de Opciones de Cuentas --\n")
    print("1. Abrir una nueva cuenta")
    print("2. Hacer una consignación")
    print("3. Hacer un retiro")
    print("4. Mostrar detalles de la cuenta")
    print("5. Salir")

def main():
    cuentas_registradas = {}
    cuenta_activa = None
    
    while True:
        mostrar_menu()
        eleccion = int(input("¿Qué te gustaría hacer? "))
        
        if eleccion == 1:
            cuenta_numero = input("Ingrese el número de cuenta: ")
            if cuenta_numero in cuentas_registradas:
                print("Error: Ya existe una cuenta con ese número.")
                continue
            cliente_nombre = input("Ingrese el nombre del cliente: ")
            balance_inicial = float(input("Ingrese el balance inicial (mínimo 100,000 pesos): "))
            nueva_cuenta = BancoCuenta()
            if nueva_cuenta.iniciar_cuenta(cuenta_numero, cliente_nombre, balance_inicial):
                cuentas_registradas[cuenta_numero] = nueva_cuenta
                cuenta_activa = nueva_cuenta
        elif eleccion == 2:
            if cuenta_activa:
                monto = float(input("Ingrese el monto a consignar: "))
                cuenta_activa.hacer_consignacion(monto)
            else:
                print("Primero debes abrir una cuenta")
        elif eleccion == 3:
            if cuenta_activa:
                monto = float(input("Ingrese el monto a retirar: "))
                cuenta_activa.hacer_retiro(monto)
            else:
                print("Primero debes abrir una cuenta")
        elif eleccion == 4:
            if cuenta_activa:
                cuenta_activa.mostrar_detalles()
            else:
                print("Primero debes abrir una cuenta")
        elif eleccion == 5:
            print("Hasta luego")
            break
        else:
            print("Opción inválida. Selecciona una opción válida del menú")
            
if __name__ == "__main__":
    main()



