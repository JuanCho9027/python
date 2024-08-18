def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero no permitida"

def calculadora():
    while True:
        print("\nSelecciona la operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("Escribe 'Salir' para terminar")

        eleccion = input("Introduce la opción (1/2/3/4) o 'Salir': ")

        if eleccion.lower() == 'salir':
            print("Saliendo de la calculadora...")
            break

        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if eleccion == '1':
            print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")
        elif eleccion == '2':
            print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
        elif eleccion == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicacion(num1, num2)}")
        elif eleccion == '4':
            print(f"Resultado: {num1} / {num2} = {division(num1, num2)}")
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 4 o escribe 'Salir'.")

# Ejecutar la calculadora
calculadora()