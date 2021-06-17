import numpy as np

matriz1=[];
matriz2=[];
matrizProducto=[]

"----------------------------------------------------"
print("\t\t\t\t\tPRIMERA MATRIZ\n")

filas=int(input("Ingrese el numero de filas: "))
columnas=int(input("Ingrese el numero de columnas: "))

for i in range (filas):   
  matriz1.append([])
  for j in range (columnas):
   valor = float (input(f'Fila {str(i+1)}, Columna {str(j+1)} : '))
   matriz1[i].append(valor)
 
print("")
print(matriz1)

"----------------------------------------------------"
print("\n\t\t\t\t\tSEGUNDA MATRIZ\n")

Fila_2da= int (input("Digite el numero de filas: "))
Columna_2da= int(input("Digite el numero de columnas: "))

for i in range (Fila_2da):

  matriz2.append([])

  for j in range (Columna_2da):

   valor_2do=float(input(f"Fila {str(i+1)}, Columna{str(j+1)} : "))
   matriz2[i].append(valor_2do)  

print("")
print(matriz2) 

"----------------------------------------------------"
print("\n\t\tPRODUCTO DE LAS DOS MATRICES INGRESADAS\n")

if columnas!= Fila_2da:
  print("No se puede multiplicar")
else:  
  matrizProducto=np.dot(matriz1, matriz2)
  print(matrizProducto)
