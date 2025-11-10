import os
import csv

#Menu Principal
def menu():
  while True:
    print("\n<-----MENU PRINCIPAL----->")
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
        agregar_pais()
      case 2:
        actualizar_datos()
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


def agregar_pais(Paises):
   with open("Paises.csv","a", newline="", encoding="utf-8") as archivo:
      escritor = csv.DictWriter(archivo,fieldnames=["Pais","Poblacion","Superficie km2","Continente"])
      escritor.writerow(Paises)

def existe_pais(nombre):
  Paises = Verificar_lista()

  for p in Paises:
    if p["Pais"].lower() == nombre.strip().lower():
      return True
  return False


def Verificar_lista():
  Paises = []
  
  if not os.path.exists("Paises.csv"):
    with open("Paises.csv", "w", newline="", encoding="utf-8") as archivo:
      escritor = csv.DictWriter(archivo, fieldnames=["Pais", "Poblacion", "Superficie km2", "Continente"])
      escritor.writeheader()
      return Paises

  with open("Paises.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
        
    for fila in lector:
          Paises.append({
            "Pais": fila["Pais"],
            "Poblacion" : float(fila["Poblacion"]),
            "Superficie km2" : float(fila["Superficie km2"]),
            "Continente" : fila["Continente"]})
    return Paises
  
def validar_numero(po):
  if po.count(".") > 1:
    return False
  if not po.replace(".","").isdigit():
    return False
  return True

def validar_palabra(entrada):
  entrada_limpia = entrada.strip()
  if not entrada_limpia:
    return False
  
  if not entrada_limpia.isalpha():
    return False
  return True

# Opcion 1  
def agregar_pais():
  while True:
   print("\n<-----Agregar nuevo pais----->")
   nombre = input("Ingrese el nombre del pais: ").strip()
   if existe_pais(nombre):
     print("Ya esta ingresado este pais")
     continue

   poblacion = input("Ingrese el numero de poblacion: ").strip()

   if not validar_numero(poblacion):
     print("Valor incorrecto. Ingrese de nuevo porfavor")
     continue
   
   poblacion = float(poblacion)

   superficie = input("Ingrese la superficie del pais en km2: ").strip()

   if not validar_numero(superficie):
     print("Valor incorrecto. Ingrese de nuevo porfavor")
     continue
   
   superficie = float(superficie)
   
   continente = input("Ingrese el continente al que pertenece: ").strip()
   
   if not validar_palabra(continente):
     print("Entrada incorrecta. Intente de nuevo por favor")
     continue

   agregar_pais({"Pais":nombre,"Poblacion":poblacion,"Superficie km2":superficie,"Continente":continente})

   continuar = input("¿Desea agregar otro pais? (s/n): ").lower().strip()
   if continuar != "s":
     break

# Opcion 2
def actualizar_datos():
  lista = Verificar_lista()

  if len(lista) == 0:
    print("No existen registros de ningun pais")
    input("Presione enter para volver al menu principal...")
    return
  
  while True:
    print ("\n<-----Actualizar datos----->")
    pais = input("Ingrese el nombre del pais (Ingrese 'salir' para volver al menu principal)").lower().strip()
    
    if pais == "salir":
      print("Volviendo al menu principal...")
      return

    if not validar_palabra(pais):
      print("Ingreso invalido, intentelo nuevamente.")
      continue

    if not existe_pais(pais):
      print("El pais no se encuentra registrado")
      continue

    for linea in lista: 
      if linea["Pais"].lower() == pais:        
        while True:
          print("\n<----- Datos actuales ----->")
          print(f"País: {linea['Pais']}")
          print(f"Población: {linea['Poblacion']}")
          print(f"Superficie: {linea['Superficie km2']} km²")
          print(f"Continente: {linea['Continente']}")

        # Elegir qué actualizar
          print("\n¿Que desea actualizar?")
          print("1) Poblacion")
          print("2) Superficie")
          print("3) Elegir otro pais")
          print("4) volver al menu principal")

          opcion = input("Opcion: ").strip()

          if not validar_numero(opcion):
            print("ERROR! Debe ingresar un numero del 1 al 4")
            continue
        
          match opcion:
            case "1":
              poblacion = input
             
            case "2":
              pass
            
            case "3":
              break
            
            case "4":
              print("Volviendo al menu principal...")
              return
            
            case _:
              print("ERROR! Debe ingresar un numero del 1 al 4")
              continue
             
          

    
    




Verificar_lista()    
agregar_pais()
