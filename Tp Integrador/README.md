Descripcion del programa

El programa es una aplicación interactiva en Python diseñada para gestionar información de países. Permite almacenar, consultar, actualizar, filtrar, ordenar y analizar datos relacionados con población, superficie y continente.
Toda la información se guarda en un archivo externo llamado “Paises.csv”, lo que permite que los datos permanezcan disponibles incluso después de cerrar el programa.

El sistema funciona a través de un menú principal, desde el cual el usuario puede acceder a distintas funciones. A continuación, se describe su funcionamiento general:

🔹 1. Agregar país

Permite incorporar un nuevo país al archivo.
El usuario ingresa:

nombre del país,

población,

superficie en km²

continente

El programa valida que el país no exista previamente y que los datos ingresados sean válidos.

🔹 2. Actualizar datos

Permite modificar la población o la superficie de un país ya registrado.
El usuario selecciona el país, elige qué dato actualizar y el programa guarda los cambios en el archivo CSV.

🔹 3. Buscar país

El usuario puede buscar un país por nombre o por coincidencia parcial.
El programa muestra una lista de resultados y permite seleccionar uno para ver todos sus datos detallados.

🔹 4. Filtro de países

Ofrece tres tipos de filtrado:

Por continente

Por rango de población

Por rango de superficie

Después del filtrado, el usuario puede ver datos del país seleccionado.

🔹 5. Ordenar países

Permite ordenar la lista de países según:

Nombre

Población

Superficie

Continente

El usuario también elige si quiere el orden creciente o decreciente.
La ordenación se realiza mediante el algoritmo burbuja (implementado manualmente).

🔹 6. Mostrar estadísticas

El programa calcula y muestra estadísticas sobre los países cargados:

País con menor y mayor población

Promedio (mediana) de población

Promedio (mediana) de superficie

Cantidad de países por continente

🔹 7. Salir

Finaliza la ejecución del programa.

📂 Manejo de archivos

El programa utiliza un archivo CSV para almacenar los datos.
Cada registro incluye:

País

Población

Superficie km²

Continente

Si el archivo no existe, se crea automáticamente con los encabezados correspondientes.

🧠 Validaciones

Para evitar errores del usuario, el programa incluye:

Verificación de que un país no se duplique

Validación de números (población y superficie)

Validación de palabras (nombres de países)

Control de opciones del menú

Manejo de listas vacías

✔️ Objetivo general

El programa permite administrar una base de datos simple pero completa de países, ofreciendo herramientas de:

Carga

modificación

búsqueda

clasificación

filtrado

análisis

Está orientado a prácticas de Python, manejo de archivos CSV, estructuras de datos, validaciones y menús interactivos.

INSTRUCCIONES 
1. Ejecutar el programa
   
Abrí el archivo TP INTEGRADOR.py en tu entorno (PyCharm, VSCode, IDLE, etc.).
Ejecutalo.
En la consola aparecerá el menú principal.

2. Uso del menú principal

El usuario debe ingresar un número del 1 al 7 para seleccionar una opción
Si se ingresa un valor incorrecto, el programa pedirá repetir la entrada.

3. Agregar un país (Opción 1)
Permite cargar un nuevo país en el sistema.

Pasos:
Ingresar el nombre del país (solo letras).
Ingresar población (número válido).
Ingresar superficie en km².
Elegir el continente mediante un número del 1 al 5.
Elegir si se desea agregar otro país.
El país queda registrado en Paises.csv.

4. Actualizar datos (Opción 2)
Permite modificar la población o la superficie de un país ya existente.

Pasos:

Ingresar el nombre del país.
Elegir qué campo actualizar:
1 población

2 superficie

3 elegir otro país

4 volver al menú principal

Ingresar el nuevo valor solicitado.
Confirmar cambios.

5. Buscar un país (Opción 3)

Permite encontrar un país por su nombre o por coincidencias parciales.

Pasos:

Ingresar el nombre o parte del nombre.
Elegir uno de los resultados mostrados.
Ver los datos completos del país.
Elegir si se desea hacer otra búsqueda

6. Filtrar países (Opción 4)
   
El usuario puede elegir entre tres filtros:
a) Filtrar por continente
Seleccionar entre América, Europa, Asia, África u Oceanía.
b) Filtrar por rango de población
Ingresar valores mínimos y máximos.
c) Filtrar por rango de superficie
Ingresar valores mínimos y máximos.
Luego se muestran los países que coinciden y se puede elegir ver los datos detallados

7. Ordenar países (Opción 5)
   
Permite ordenar la lista según:

Nombre
Población
Superficie
Continente

Luego se elige el tipo de orden:
1 → Creciente
2 → Decreciente

Finalmente se muestra el listado ordenado y se puede seleccionar un país para ver sus datos.

8. Mostrar estadísticas (Opción 6)

El usuario puede ver:
País con menor y mayor población
Promedio de población
Promedio de superficie
Cantidad de países por continente
Solo debe ingresar el número correspondiente a la estadística deseada.

9. Salir del programa (Opción 7)

Finaliza la ejecución y cierra el menú.
