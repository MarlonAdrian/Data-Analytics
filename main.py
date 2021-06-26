"----------MARLON ADRIAN TUQUERRES ROMERO--------------"

"--------------------MATRIZ DE 4X4-------------------------"
matriz=[
  [21,12,21,87],
  [1,3,4,2],
  [1,14,1,8],
  [2,2,5,7],
]
print ("Matriz de 4x4\n\n"+str(matriz)+"\n\n")

filas=len(matriz)
columnas=len(matriz[0])
"-------------------SUMATORIA DE FILA Y COLUMNA------------------------"
fila= int (input("Numero de fila a sumar: "))

for i in range(filas):  
  suma=sum(matriz[fila])

print(str(suma))

columna =int (input("Numero de columna a sumar: "))

for j in range (columnas):
  suma=sum([fila[columna] for fila in matriz])

print(suma)   
"-----------MULTIPLICACION Y SUMATORIA DE LAS DIAGONALES----------"
MATRIZ=[
    [21,12,21,87],
    [1,3,4,2],
    [1,14,1,8],
    [2,2,5,7],
        ]
print("Multiplicacion de la diagonal principal de la matriz")
print(MATRIZ[0][0]*MATRIZ[1][1]*MATRIZ[2][2]*MATRIZ[3][3])

print("Sumatoria de la diagonal principal de la matriz")
print(MATRIZ[0][0]+MATRIZ[1][1]+MATRIZ[2][2]+MATRIZ[3][3])


"---------MULTIPLICACION DE LAS FILAS Y DE LAS COLUMNAS--------"
MATRIZ=[
    [21,12,21,87],
    [1,3,4,2],
    [1,14,1,8],
    [2,2,5,7],
        ]

filaProducto=int (input("Numero de fila a multiplicar: "))

if filaProducto == 0:
	print(MATRIZ[0][0]*MATRIZ[0][1]*MATRIZ[0][2]*MATRIZ[0][3])
  

else:
	if filaProducto == 1:
		print(MATRIZ[1][0]*MATRIZ[1][1]*MATRIZ[1][2]*MATRIZ[1][3])
	else:
		if filaProducto == 2:
			print(MATRIZ[2][0]*MATRIZ[2][1]*MATRIZ[2][2]*MATRIZ[2][3])
		else:
			if filaProducto == 3:
				print(MATRIZ[3][0]*MATRIZ[3][1]*MATRIZ[3][2]*MATRIZ[3][3])

MATRIZ=[
    [21,12,21,87],
    [1,3,4,2],
    [1,14,1,8],
    [2,2,5,7],
        ]
columnaProducto=int (input("Numero de columna a multiplicar: "))

if columnaProducto == 0:
	print(MATRIZ[0][0]*MATRIZ[1][0]*MATRIZ[2][0]*MATRIZ[3][0])
else:
	if columnaProducto == 1:
		print(MATRIZ[0][1]*MATRIZ[1][1]*MATRIZ[2][1]*MATRIZ[3][1])
    
	else:
		if columnaProducto == 2:
			print(MATRIZ[0][2]*MATRIZ[1][2]*MATRIZ[2][2]*MATRIZ[3][2])
      
		else:
			if columnaProducto == 3:
				print(MATRIZ[0][3]*MATRIZ[1][3]*MATRIZ[2][3]*MATRIZ[3][3])
        
"--------------------------------------------------------"




