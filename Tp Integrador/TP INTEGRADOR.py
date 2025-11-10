def menu():
    while True:
        print("<-----MENU PRINCIPAL----->")
        print("1. Agregar país")
        print("2. Actualizar datos de población y superficie de un país")
        print("3. Buscar un país por nombre ")
        print("4. Filtrar países") # Segun continente, rango de población, rango de superficie.
        print("5. Ordenar países") # Segun nombre, población, superficie (ascendente o descendente).
        print("6. Mostrar estadísticas") 
        print("7. Salir")

        while True:
            opcion = input("Elegí una opción: ")

            if not opcion.isdigit():
                print("Debes ingresar un número válido")
                continue

            opcion = int(opcion)
            break

        match opcion:
            case 1:
                pass

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass

            case 6:
                pass

            case 7:
                print("¡Hasta luego!")
                return
        
            case _:
                print("Opción inválida. Intenta nuevamente.")