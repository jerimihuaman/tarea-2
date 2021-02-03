numero_uno = float(input("Escriba el primer número: "))
numero_dos = float(input("Escriba el segundo número: "))
numero_tres = float(input("Escriba el tercer número: "))
if numero_uno>numero_dos>numero_tres:
    print(f"El número mayor es: {numero_uno} ")
    print(f"El número menor es: {numero_tres} ")
elif numero_uno>numero_tres>numero_dos:
    print(f"El número mayor es: {numero_uno} ")
    print(f"El número menor es: {numero_dos} ")
elif numero_dos>numero_tres>numero_uno:
    print(f"El número mayor es: {numero_dos} ")
    print(f"El número menor es: {numero_uno} ")
elif numero_dos>numero_uno>numero_tres:
    print(f"El número mayor es: {numero_dos} ")
    print(f"El número menor es: {numero_tres} ")
elif numero_tres>numero_dos>numero_uno:
    print(f"El número mayor es: {numero_tres} ")
    print(f"El número menor es: {numero_uno} ")
elif numero_tres>numero_uno>numero_dos:
    print(f"El número mayor es: {numero_tres} ")
    print(f"El número menor es: {numero_dos} ")
else:
    print("Debe ingresar valores distintos")