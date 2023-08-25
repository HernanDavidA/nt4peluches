peluches=["roshi", "conejito", "dragon"]
# print(peluches[2])
opcion=0
print("Pelucheria PELUCHITOS")
print("..........")
print("1. Agregar producto a la bodega")
print("2. Ver productos en stock")
print("3. Obtener valor del inventario")
print("4. Ver prodcutos mas vendidos")
print("5. SALIR")
while(opcion!=5):
    # print(peluches[1])
    # opcion = opcion+1
    opcion= int(input("Digita un numero: "))
    if opcion == 1:
        print("Usted está en la opcion 1")
    elif opcion == 2:
        print("Usted está en la opcion 2")
    elif opcion == 3:
        print("Usted está en la opcion 3")
    elif opcion == 4:
        print("Usted está en la opcion 4")
    elif opcion == 5:
        print("Has salido del programa")
    elif opcion <= 0 or opcion >= 6:
        print("Escoja una opción válida")

print("sali del ciclo")
   