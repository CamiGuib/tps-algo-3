# Idea: Me base en la idea del algoritmo de Floyd-Warshall. Fui agregando las esquinas en el mismo orden en el que fueron agregads historicamente, 
# y cada vez que agregue una esquina me fije si cada una de las distancias nodo-nodo mejoraban o no al considerar que paso por esa esquina nueva.
# De esa forma para cada esquina k agregada fui actualizando la matriz con las mejores distancias nodo-nodo encontradas hasta el momento. 
# Y para cada una de esas matrices calcule la suma de todos los valores M[i][j] donde i,j pertenecen al conjunto de las esquinas ya agregadas. 


import copy


# Funcion que suma los valores M[i][j] para i, j pertenecientes a un conjunto fila_col
def suma_matriz(M, fila_col): 
    res = 0 
    for i in fila_col:
        for j in fila_col: 
            res += M[i][j]
    return res 

 
def desarrollo(n,d,orden): 
    res = []
    orden_invertido = orden[::-1] # Invierto el orden para ir agregando las esquinas en el mismo orden en el que fueron agregadas historicamente 
    M = copy.deepcopy(d) 
    esq_agregadas = []
    
    for k in orden_invertido:    
        esq_agregadas.append(k)
        # Actualizo la matriz M 
        for i in range(n):
            for j in range(n): 
                M[i][j] = min(M[i][j] , M[i][k] + M[k][j])
        # Hago la suma de los valores de la matriz teniendo en cuenta solamente las esquinas que fueron agregadas hasta ahora 
        res.append(suma_matriz(M,esq_agregadas))

    return res[::-1]


# Leo el input
n = int(input())
d = []
for i in range(n):
    fila = list(map(int, input().split()))
    d.append(fila)
orden = list(map(int, input().split()))
 
orden = [x - 1 for x in orden]
 
# Imprimo el output
res = desarrollo(n, d, orden)
print(*res)





