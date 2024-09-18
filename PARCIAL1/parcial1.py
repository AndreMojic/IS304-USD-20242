def es_primo(num):
    """Determina si un número es primo."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def lista_primos(limite):
    """Genera una lista de números primos menores o iguales al límite dado."""
    primos = []
    for i in range(2, limite + 1):
        if es_primo(i):
            primos.append(i)
    return primos

def main():
    try:
        numero = int(input("Introduce un número entero: "))
        primos = lista_primos(numero)
        print(f"Números primos menores o iguales a {numero}: {primos}")
    except ValueError:
        print("Por favor, introduce un número entero válido.")

if __name__ == "__main__":
    main()

