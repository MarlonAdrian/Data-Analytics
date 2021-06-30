import numpy as np

"Generar un array generico Gaussiano de dos dimensiones"

X, Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
D = np.sqrt(X*X+Y*Y)
sigma, mu = 1.0, 0.0
G = np.exp(-( (D-mu)**2 / ( 2.0 * sigma**2 ) ) )
print(G)

"¿Cómo colocar aleatoriamente p elementos en una matriz 2D?" 
n = 10
p = 3
Z = np.zeros((n,n))
np.put(Z, np.random.choice(range(n*n), p, replace=False),1)

"Restar la media de cada fila de una matriz" 
X = np.random.rand(5, 10)
Y = X - X.mean(axis=1, keepdims=True)
Y = X - X.mean(axis=1).reshape(-1, 1)

"¿Cómo ordenar una matriz por la enésima columna "
Z = np.random.randint(0,10,(3,3))
print(Z)
print(Z[Z[:,1].argsort()])

"¿Cómo saber si una matriz 2D dada tiene columnas nulas?"
Z = np.random.randint(0,3,(3,10))
print((~Z.any(axis=0)).any())

"Encuentre el valor más cercano de un valor dado en una matriz"
Z = np.random.uniform(0,1,10)
z = 0.5
m = Z.flat[np.abs(Z - z).argmin()]
print(m)

"¿Cómo imprimir todos los valores de un array?"
np.set_printoptions(threshold=np.nan)
Z = np.zeros((25,25))
print(Z)

"¿Cómo encontrar el valor más cercano (a un escalar dado) en una matriz?"
Z = np.arange(100)
v = np.random.uniform(0,100)
index = (np.abs(Z-v)).argmin()
print(Z[index])

"Crear un vector de tamaño 10, con valores que oscilen entre 0 a 1 (ambos excluidos)" 
Z = np.linspace(0,1,12,endpoint=True)[1:-1]
print(Z)

"Crear un vector randómico de tamaño 10 y ordenarlo"
Z = np.random.random(10)
Z.sort()
print(Z)

"¿Cómo sumar un array pequeño mas rápido que un np.sum"
Z = np.arange(10)
np.add.reduce(Z)

"Considerar dos arrays randómicos (A y B), verifique si estos son iguales"
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.allclose(A,B)
print(equal)

"Hacer una matriz inmutable (solo lectura)"
Z = np.zeros(10)
Z.flags.writeable = False
Z[0] = 1

"Considere una matriz aleatoria de 10 x 2 que represente coordenadas cartesianas, conviértalas a coordenadas polares"
Z = np.random.random((10,2))
X,Y = Z[:,0], Z[:,1]
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
print(R)
print(T)

"¿Cómo redondear desde cero una matriz flotante?"
Z = np.random.uniform(-10,+10,10)
print (np.trunc(Z + np.copysign(0.5, Z)))
