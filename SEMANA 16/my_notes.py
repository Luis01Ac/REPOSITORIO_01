# Nombre del archivo
filename = 'my_notes.txt'

# Vamos a crear y escribir en el archivo my_notes.txt
# Abrimos el archivo en modo escritura
file = open(filename, 'w')  # 'w' nos indica que estamos abriendo el archivo para escribir
# Escribimos notas personales en el archivo
file.write("Revisar los planos y detalles tecnicos.\n")  # Línea 1
file.write("Reunion con los diferentes tecnicos del proyecto.\n")       # Línea 2
file.write("Actualizar el cronograma de los proyectos.\n")        # Línea 3
file.write("Verificar el progreso de cada area del proyecto.\n")        # Línea 4
# Cerramos el archivo después de escribir
file.close()  # Cierra el archivo después de la escritura

# Leer el archivo my_notes.txt
# Abrimos el archivo en modo lectura
file = open(filename, 'r')  # 'r' indica que estamos abriendo el archivo para leer
# Leemos el archivo línea por línea
while True:
    line = file.readline()  # Leemos una línea del archivo
    if not line:  # Si no hay más líneas, salimos del bucle
        break
    # 5. Mostramos en la consola cada línea leída
    print(line.strip())  # strip() elimina el salto de línea al final

# 6. Cierre del archivo después de la lectura
file.close()  # Cierre del archivo