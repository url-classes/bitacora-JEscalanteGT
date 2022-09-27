def factorial(n: int):
    # Paso base
    if n == 1:
        return 1
    # Paso recursivo
    else:
        resultado = n * factorial(n)
        return resultado


def main():
    n = int(input('Ingrese un número: '))
    print(factorial(n))


main()
