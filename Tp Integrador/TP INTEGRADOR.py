import os
import csv

def agregar_Pais(Paises):
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
  
def agregar_datospais():
  while True:
   print("---Agregar nuevo pais---")
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

   agregar_Pais({"Pais":nombre,"Poblacion":poblacion,"Superficie km2":superficie,"Continente":continente})

   continuar = input("¿Desea agregar otro pais? (s/n): ").lower().strip()
   if continuar != "s":
     break


Verificar_lista()    
agregar_datospais()

