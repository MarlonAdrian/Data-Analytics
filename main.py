print("\t\t\t\t\tPRIMERA MATRIZ\n")

filas= int (input("Digite el numero de filas: "))
columnas= int (input("Digite el numero de columnas: "))

matriz=[]
matriz_2da=[]
MATRIZ_PRODUCTO=[]

for i in range (filas):   
  matriz.append([])
  for j in range (columnas):
   valor = float (input(f'Fila {str(i+1)}, Columna {str(j+1)} : '))
   matriz[i].append(valor)

print("")
print(matriz) 

"-----------------------------------------------------"
print("\n\t\t\t\t\tSEGUNDA MATRIZ\n")

Fila_2da= int (input("Digite el numero de filas: "))
Columna_2da= int(input("Digite el numero de columnas: "))

for i2 in range (Fila_2da):

  matriz_2da.append([])

  for j2 in range (Columna_2da):

   valor_2do=float(input(f"Fila {str(i2+1)}, Columna{str(j2+1)} : "))
   matriz_2da[i2].append(valor_2do)  

print("")
print(matriz_2da) 

"-----------------------------------------------------"
print("\n\t\tPRODUCTO DE LAS DOS MATRICES INGRESADAS\n")
if columnas!= Fila_2da:
  print("No se puede multiplicar")
else:  
 for k in range(filas):
   MATRIZ_PRODUCTO.append([0]*Columna_2da)
   for i in range(Columna_2da):
     MATRIZ_PRODUCTO[k][i]=0

 for i in range (filas):
   for j in range(columnas):
     for k in range (Columna_2da):
       MATRIZ_PRODUCTO[i][k]= MATRIZ_PRODUCTO[i][k] + (matriz[i][j]*matriz_2da[j][k]) 

 print(MATRIZ_PRODUCTO)
