# RECORDATORIOS
# - Solo queda hacer la opcion 6 (mostrar estadisticas) del menu

import os
import csv

#Menu Principal
def menu():
  while True:
    print("\n<-----MENU PRINCIPAL----->")
    print("1. Agregar país")
    print("2. Actualizar datos de población y superficie de un país")
    print("3. Buscar un país por nombre ")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas") 
    print("7. <-- Salir")

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
        buscar_pais()
      case 4:
        filtro()
      case 5:
        ordenar_paises()
      case 6:
        mostrar_estadisticas()
      case 7:
        print("¡Hasta luego!")
        return
      case _:
        print("Opción inválida. Intenta nuevamente.")

# Guardar datos en Paises.csv
def guardar_cambios(lista):
    with open("Paises.csv", "w", encoding="utf-8", newline="") as archivo:
        
        archivo.write("Pais,Poblacion,Superficie km2,Continente\n")
  
        for diccionario in lista:
            archivo.write(
                f"{diccionario['Pais']},"
                f"{diccionario['Poblacion']},"
                f"{diccionario['Superficie km2']},"
                f"{diccionario['Continente']}\n"
            )

# Agrega un pais a Paises.csv
def agregar_pais_csv(Paises):
   with open("Paises.csv","a", newline="", encoding="utf-8") as archivo:
      escritor = csv.DictWriter(archivo,fieldnames=["Pais","Poblacion","Superficie km2","Continente"])
      escritor.writerow(Paises)

# Verifica que un pais se encuentre en el archivo
def existe_pais(nombre):
  Paises = Verificar_lista()

  for p in Paises:
    if p["Pais"].lower() == nombre.strip().lower():
      return True
  return False

# Cargar datos de Paises.csv en una lista
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

# Verificar que solo son numeros (pueden tener hasta un ".")
def validar_numero(po):
  if po.count(".") > 1:
    return False
  if not po.replace(".","").isdigit():
    return False
  return True

# Verificar que solo son letras (puede tener espacios)
def validar_palabra(entrada):
    entrada_limpia = entrada.strip()

    if not entrada_limpia:
        return False
    
    if not entrada_limpia.replace(" ", "").isalpha():
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
   
   print("Seleccione el continente al que pertenece: ") 
   print("1. America")
   print("2. Europa")
   print("3. Asia")
   print("4. Africa")
   print("5. Oceania")
   continente = int(input().strip())
   match continente:
     case 1:
       continente = "America"
     case 2:
       continente = "Europa"
     case 3:
       continente = "Asia"
     case 4:
       continente = "Africa"
     case 5:
       continente = "Oceania"
     case _:
       print("Opcion invalida. Intente de nuevo por favor")
       continue

   agregar_pais_csv({"Pais":nombre,"Poblacion":poblacion,"Superficie km2":superficie,"Continente":continente})

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
    pais = input("Ingrese el nombre del pais (o 'salir' para volver al menu principal): ").lower().strip()
    
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

          print("\n¿Que desea actualizar?")
          print("1) Poblacion")
          print("2) Superficie")
          print("3) Elegir otro pais")
          print("4) <-- volver al menu principal")

          opcion = input("Opcion: ").strip()

          if not validar_numero(opcion):
            print("ERROR! Debe ingresar un numero del 1 al 4")
            continue
        
          match opcion:
            case "1":
              print(f"Poblacion actual de {linea['Pais'].title()}: {linea['Poblacion']} habitantes")
              while True:
                poblacion = input("Ingrese la nueva cantidad: ")

                if not validar_numero(poblacion):
                  print("Debe ingresar un numero entero")
                  continue
                else:
                  break

              linea['Poblacion'] = poblacion
              guardar_cambios(lista)
              print("Los cambios se guardaron exitosamente")
              input("Presione enter para continuar...")
              continue

            case "2":
              print(f"Superficie actual de {linea['Pais'].title()}: {linea['Superficie km2']} km²")
              while True:
                superficie = input("Ingrese la nueva superficie: ")

                if not validar_numero(superficie):
                  print("Debe ingresar solo numeros")
                  continue
                else:
                  break

              linea['Superficie km2'] = superficie
              guardar_cambios(lista)
              print("Los cambios se guardaron exitosamente")
              input("Presione enter para continuar...")
              continue

            case "3":
              break
            
            case "4":
              print("Volviendo al menu principal...")
              return
            
            case _:
              print("ERROR! Debe ingresar un numero del 1 al 4")
              continue

# Opcion 3     
def buscar_pais():
  lista = Verificar_lista()
  
  if len(lista) == 0:
    print("No existen registros de ningun pais")
    input("Presione enter para volver al menu principal...")
    return

  while True:
    resultados = []
    contador = 0
    print("\n<----- Buscar pais ----->")
    pais = input("Ingrese el nombre del pais (o 'salir' para volver al menu principal): ").lower().strip()

    if pais == "salir":
      print("Volviendo al menú principal...")
      return
         
    if not validar_palabra(pais):
      print("Ingreso invalido, intentelo nuevamente.")
      continue

    for linea in lista:
      if pais.lower() in linea['Pais'].lower():
        if contador == 0:
          print(f"Resultados de '{pais}':")

        contador +=1
        print(f"{contador}. {linea['Pais'].title()}")

        resultados.append({'pais' : linea['Pais'], 'poblacion' : linea['Poblacion'], 'superficie' : linea['Superficie km2'], 'continente' : linea['Continente']})

    if len(resultados) == 0:
      print(f"No existen coincidencias con '{pais}', intentelo nuevamente")
      continue
    
    while True:
      opcion = input(f"Elija el resultado que desea: ")

      if not validar_numero(opcion):
        print("ERROR! Debe ingresar un numero")
        continue
      
      opcion = int(opcion)

      if not 0 < opcion <= len(resultados):
        print("ERROR! El numero no se encuentra en el rango permitido")
        print("Intentelo nuevamente")
        continue

      else:
        break       
    print(f"\nPaís: {resultados[opcion - 1]['pais'].title()}")
    print(f"Población: {resultados[opcion - 1]['poblacion']}")
    print(f"Superficie: {resultados[opcion - 1]['superficie']} km²")
    print(f"Continente: {resultados[opcion - 1]['continente']}")
    
    opcion = input("\n¿Quiere consultar los datos de otro pais? S/N")

    if opcion.lower() == "s":
      continue

    else:
      return

# Opcion 4
def filtro():
  lista = Verificar_lista()
  
  if len(lista) == 0:
    print("No existen registros de ningun pais")
    input("Presione enter para volver al menu principal...")
    return
  
  while True:
    print("\n<-----FILTRAR PAISES----->")
    print("Filtrar segun:")
    print("1. Continente")
    print("2. Poblacion")
    print("3. Superficie")
    print("4. <-- Volver al menu principal")

    while True:
        opcion = input("Elegí una opción: ")

        if not opcion.isdigit():
          print("Debes ingresar un número válido")
          continue

        opcion = int(opcion)
        break

    match opcion:
      case 1:
        filtro_1(lista)
      case 2:
        filtro_2(lista)
      
      case 3:
        filtro_3(lista)
      
      case 4:
        print("Volviendo al menu principal...")
        return
      
      case _:
        print("Opción inválida. Intenta nuevamente.")

# Filtro opcion 1 (Segun continente)
def filtro_1(lista):
  continentes = ["america", "europa", "asia", "africa", "oceania"]
  while True:
    print("\n<-----FILTRADO POR CONTINENTES----->")
    print("Filtrar paises en:")
    print("1. America")
    print("2. Europa")
    print("3. Asia")
    print("4. Africa")
    print("5. Oceania")
    print("6. <-- Volver a al menu de filtros")

    while True:
        resultados = []
        contador = 0
        opcion = input("Elegí una opción: ")

        if not opcion.isdigit():
          print("Debes ingresar un número válido")
          input("Presione enter para vovler a intentarlo...")
          continue

        opcion = int(opcion)

        if not 0 < opcion <=6:
          print("ERROR! Debe ingresar un numero del 1 al 6")
          continue
        
        break
    
    if opcion == 6:
      break
    
    for diccionario in lista:
      if diccionario['Continente'].lower() == continentes[opcion - 1]:
        if contador == 0:
          print(f"Resultados de paises en {continentes[opcion - 1].title()}:")

        contador +=1
        print(f"{contador}. {diccionario['Pais'].title()}")

        resultados.append({'pais' : diccionario['Pais'], 'poblacion' : diccionario['Poblacion'], 'superficie' : diccionario['Superficie km2'], 'continente' : diccionario['Continente']})

    if len(resultados) == 0:
      print(f"No existen paises cargados en {continentes[opcion - 1]}")
      continue
    
    while True:
      opcion = input(f"Elija el resultado que desea: ")

      if not validar_numero(opcion):
        print("ERROR! Debe ingresar un numero")
        continue
      
      opcion = int(opcion)

      if not 0 < opcion <= len(resultados):
        print("ERROR! El numero no se encuentra en el rango permitido")
        print("Intentelo nuevamente")
        continue

      else:
        break       
    print(f"\nPaís: {resultados[opcion - 1]['pais'].title()}")
    print(f"Población: {resultados[opcion - 1]['poblacion']}")
    print(f"Superficie: {resultados[opcion - 1]['superficie']} km²")
    print(f"Continente: {resultados[opcion - 1]['continente']}")
    
    while True:
      opcion = input("\n¿Quiere utilizar otro continente? S/N").lower()

      if opcion == "n" or opcion == "s":
        break
      else:
        print("ERROR! Solo puede ingresar 'S' o 'N'")

    if opcion.lower() == "n":
      return

# Filtro opcion 2 (Segun rango de poblacion)
def filtro_2(lista):
   while True:
    resultados = []
    print("\n<-----FILTRADO POR RANGO DE POBLACION----->")
    print("(Ingrese 'salir' para volver al menu de filtros)")

    minimo = input("Ingrese el minimo: ").strip()

    if minimo.lower() == "salir":
      print("Volviendo al menu de filtros")
      return
    
    if not minimo.isdigit():
      print("ERROR! Debe ingresar un numero entero")
      print("Intentelo nuevamente")
      continue

    maximo = input("Ingrese el maximo: ").strip()
    if maximo.lower() == "salir":
      print("Volviendo al menu de filtros")
      return
    
    if not maximo.isdigit():
      print("ERROR! Debe ingresar un numero entero")
      print("Intentelo nuevamente")
      continue
    
    minimo = int(minimo)
    maximo = int(maximo)

    if minimo >= maximo:
      print("ERROR! El valor minimo no puede ser mayor o igual al maximo.")
      print("Intentelo nuevamente")
      continue

    contador = 0
    for diccionario in lista:
      if minimo <= diccionario['Poblacion'] <= maximo:
        if contador == 0:
          print(f"\nPaíses con población entre {minimo} y {maximo}:")

        contador += 1
        print(F"{contador}. {diccionario['Pais'].title()}: {diccionario ['Poblacion']} habitantes")
        resultados.append(diccionario)

    if contador == 0:
      
      print(f"\nNo se encontraron países con población entre {minimo} y {maximo}.")
      print("1. Volver a intentarlo")
      print("2. <-- Volver al menu de filtros")

      while True:
        opcion = input("Opcion: ").strip()

        if opcion not in ("1", "2"):
          print("ERROR! Debe ingresar '1' o '2'")
          print("Intentelo nuevamente")
          continue
        break

      if int(opcion) == 1:
        continue
      else:
        return
    
    while True:
      opcion = input(f"Elija el resultado que desea: ")

      if not opcion.isdigit():
        print("ERROR! Debe ingresar un número entero")
        continue

      
      opcion = int(opcion)

      if not 0 < opcion <= len(resultados):
        print("ERROR! El numero no se encuentra en el rango permitido")
        print("Intentelo nuevamente")
        continue

      else:
        break       
    print(f"\nPaís: {resultados[opcion - 1]['Pais'].title()}")
    print(f"Población: {resultados[opcion - 1]['Poblacion']}")
    print(f"Superficie: {resultados[opcion - 1]['Superficie km2']} km²")
    print(f"Continente: {resultados[opcion - 1]['Continente']}")
    
    while True:
      opcion = input("\n¿Quiere utilizar otro rango de poblacion? S/N").lower()

      if opcion == "n" or opcion == "s":
        break
      else:
        print("ERROR! Solo puede ingresar 'S' o 'N'")

    if opcion == "n":
      return

# Filtro opcion 3 (Segun rango de superficie)
def filtro_3(lista):
  while True:
    resultados = []
    print("\n<-----FILTRADO POR RANGO DE SUPERFICIE----->")
    print("(Ingrese 'salir' para volver al menu de filtros)")

    minimo = input("Ingrese el minimo en km²: ").strip()

    if minimo.lower() == "salir":
      print("Volviendo al menu de filtros")
      return
    
    if not validar_numero(minimo):
      print("ERROR! Debe ingresar un numero")
      print("Intentelo nuevamente")
      continue

    maximo = input("Ingrese el maximo en km²: ").strip()
    if maximo.lower() == "salir":
      print("Volviendo al menu de filtros")
      return
    
    if not validar_numero(maximo):
      print("ERROR! Debe ingresar un numero")
      print("Intentelo nuevamente")
      continue
    
    minimo = float(minimo)
    maximo = float(maximo)

    if minimo >= maximo:
      print("ERROR! El valor minimo no puede ser mayor o igual al maximo.")
      print("Intentelo nuevamente")
      continue

    contador = 0
    for diccionario in lista:
      if minimo <= diccionario['Superficie km2'] <= maximo:
        if contador == 0:
          print(f"\nPaíses con superficie entre {minimo} km² y {maximo} km²:")

        contador += 1
        print(F"{contador}. {diccionario['Pais'].title()} --> Superficie: {diccionario ['Superficie km2']} km²")
        resultados.append(diccionario)

    if contador == 0:
      
      print(f"\nNo se encontraron países con superficie entre {minimo} km² y {maximo} km².")
      print("1. Volver a intentarlo")
      print("2. <-- Volver al menu de filtros")

      while True:
        opcion = input("Opcion: ").strip()

        if opcion not in ("1", "2"):
          print("ERROR! Debe ingresar '1' o '2'")
          print("Intentelo nuevamente")
          continue
        break

      if int(opcion) == 1:
        continue
      else:
        return
    
    while True:
      opcion = input(f"Elija el resultado que desea: ")

      if not opcion.isdigit():
        print("ERROR! Debe ingresar un número entero")
        continue

      
      opcion = int(opcion)

      if not 0 < opcion <= len(resultados):
        print("ERROR! El numero no se encuentra en el rango permitido")
        print("Intentelo nuevamente")
        continue

      else:
        break       
    print(f"\nPaís: {resultados[opcion - 1]['Pais'].title()}")
    print(f"Población: {resultados[opcion - 1]['Poblacion']}")
    print(f"Superficie: {resultados[opcion - 1]['Superficie km2']} km²")
    print(f"Continente: {resultados[opcion - 1]['Continente']}")
    
    while True:
      opcion = input("\n¿Quiere utilizar otro rango de superficie? S/N").lower()

      if opcion == "n" or opcion == "s":
        break
      else:
        print("ERROR! Solo puede ingresar 'S' o 'N'")

    if opcion == "n":
      return

# Opcion 5
def ordenar_paises():

  lista = Verificar_lista()
  keys = { 1: "Pais", 2: "Poblacion", 3: "Superficie km2", 4: "Continente"}
  
  if len(lista) == 0:
    print("No existen registros de ningun pais")
    input("Presione enter para volver al menu principal...")
    return
  
  while True:
    print("\n<-----ORDENAR----->")
    print("Ordenar segun:")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    print("4. Continente")
    print("5. <-- Volver al menu principal")

    opcion_key = input("Opcion: ")

    if not opcion_key.isdigit() or opcion_key not in ("1", "2", "3", "4", "5"):
        print("ERROR! Debe ingresar un número entero del 1 al 5")
        continue
    
    opcion_key = int(opcion_key)

    if opcion_key == 5:
      print("Volviendo al menu principal...")
      return

    key = keys[opcion_key]

    print (f"\n<------ORDENAR SEGUN {key.upper()}------>")
    print("Ordenar de forma:")
    print("1. Creciente")
    print("2. Decreciente")
    print("3. <-- Volver al menu anterior")

    while True:

      opcion_orden = input("Opcion: ")

      if not opcion_orden.isdigit() or opcion_orden not in ("1", "2", "3"):
        print("ERROR! Debe ingresar un número entero del 1 al 3")
        continue

      else:
        break
    
    if opcion_orden == "3":
      print("Volviendo al menu anterior...")
      continue

    orden = "creciente" if opcion_orden == "1" else "decreciente"

    lista_ordenada = ordenar_lista(lista, key, orden)

    print(f"LISTADO DE PAISES ORDENADOS DE FORMA {orden.upper()} SEGUN {key.upper()}")
    
    contador = 1

    for diccionario in lista_ordenada:

      print(f"{contador}. {diccionario['Pais']} --> {key}: {diccionario[key]} ")
      contador += 1
    
    print(f"{contador}) <-- Volver al menu anterior")

    while True:

      opcion_pais = input("Opcion: ")

      if not opcion_pais.isdigit():
        print(f"ERROR! Debe ingresar un número del 1 al {contador}")
        continue

      opcion_pais = int(opcion_pais)

      if not 1 <= opcion_pais <= contador:
        print(f"ERROR! Debe ingresar un número del 1 al {contador}")
        continue


      else:
        break

    if contador == opcion_pais:
      print("Volviendo al menu anterior...")
      continue

    print(f"\n<-----{lista_ordenada[opcion_pais - 1]['Pais']}----->")
    print(f"Población: {lista_ordenada[opcion_pais - 1]['Poblacion']}")
    print(f"Superficie: {lista_ordenada[opcion_pais - 1]['Superficie km2']} km²")
    print(f"Continente: {lista_ordenada[opcion_pais - 1]['Continente']}")

    while True:
      opcion = input("\n¿Quiere buscar otro pais? S/N").lower()

      if opcion == "n" or opcion == "s":
        break
      else:
        print("ERROR! Solo puede ingresar 'S' o 'N'")

    if opcion == "n":
      print("Volviendo al menu principal...")
      return

# Ordenar una lista mediante el metodo burbuja
def ordenar_lista(lista_desordenada, key, orden):

    lista_ordenada = lista_desordenada.copy()
    n = len(lista_ordenada)

    for i in range(n - 1):
        for j in range(n - 1 - i):

            x = lista_ordenada[j][key]
            y = lista_ordenada[j + 1][key]

            if orden == "creciente" and x > y:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]

            elif orden == "decreciente" and x < y:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]

    return lista_ordenada

# Opcion 6
def mostrar_estadisticas():

  Paises = Verificar_lista()
  print("<-----ESTADISTICAS DE PAISES----->")
  print("Seleccione la estadística que desea ver:")
  print("1. País con menor y mayor población")
  print("2. Promedio de población")
  print("3. Promedio de superficie")
  print("4. Cantidad de países por continente")

  opcion = input("Ingrese el opcion que desea ver: ")
  if not opcion.isdigit():
    print("Debes ingresar un número válido")
    return
  opcion = int(opcion)

  match opcion:
    case 1:
      pais_menor_y_mayor_poblacion(Paises)
    case 2:
      promedio_poblacion(Paises)
    case 3:
      promedio_superficie(Paises)
    case 4:
      cantidad_paises_por_continente(Paises)
    case _:
      print("Opción inválida. Intenta nuevamente.")

def pais_menor_y_mayor_poblacion(Paises):
 Paises = Verificar_lista()
 if len(Paises) == 0:
   print("No existen registros de ningun pais")
   input("Presione enter para volver al menu principal...")
   return
   
 pais_min = Paises[0]
 pais_max = Paises[0]

 min_poblacion = Paises[0]["Poblacion"]
 max_poblacion = Paises[0]["Poblacion"]

 for pais in Paises:
    if pais["Poblacion"] < min_poblacion:
      min_poblacion = pais["Poblacion"]
      pais_min = pais
    if pais["Poblacion"] > max_poblacion:
      max_poblacion = pais["Poblacion"]
      pais_max = pais

 print("-" * 30)
 print(f"País con menor población: {pais_min['Pais']}")
 print(f"Población: {pais_min['Poblacion']:,.0f} habitantes")
 print("-" * 30)
 print(f"País con mayor población: {pais_max['Pais']}")
 print(f"Población: {pais_max['Poblacion']:,.0f} habitantes")

def promedio_poblacion(Paises):
 Paises = Verificar_lista()
 if len(Paises) == 0:
   print("No existen registros de ningun pais")
   input("Presione enter para volver al menu principal...")
   return

 total_poblacion = sum(pais["Poblacion"] for pais in Paises)
 promedio = total_poblacion / len(Paises)

 print("-" * 30)
 print(f"Promedio de población: {promedio:,.0f} habitantes")
 return


def promedio_superficie(Paises):
 Paises = Verificar_lista()
 if len(Paises) == 0:
    print("No existen registros de ningun pais")
    input("Presione enter para volver al menu principal...")
    return
  
 total_superficie = sum(pais["Superficie km2"] for pais in Paises)
 promedio = total_superficie / len(Paises)
  
 print("-" * 30)
 print(f"Promedio de superficie: {promedio:,.2f} km²")

def cantidad_paises_por_continente(Paises):
  Paises = Verificar_lista()
  if len(Paises) == 0:
      print("No existen registros de ningun pais")
      input("Presione enter para volver al menu principal...")
      return
  
  continente_count = {}
  
  for pais in Paises:
      continente = pais["Continente"]
      if continente in continente_count:
        continente_count[continente] += 1
      else:
        continente_count[continente] = 1
  
  print("-" * 30)
  print("Cantidad de países por continente:")
  for continente, count in continente_count.items():
      print(f"{continente}: {count} país/es")
  return

menu()
