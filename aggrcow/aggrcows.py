# Idea: 
# Hare una busqueda binaria con el objetivo de encontrar la distancia optima. 
# A la busqueda binaria la comenzare usando como limite inferior (inf) el valor 0 (pues distancia menor a eso es imposible) y como limite superior (sup) a la distancia entre el ultimo y el primer establo (pues distancia mayor a esa es imposible)
# En cada paso chequeo con una funcion de verificacion si es posible acomodar a las C vacas a esa dada distancia
# Si es posible, probamos con una distancia mayor
# Si no es posible, probamos con una distancia menor



# Funcion principal
def aggrcow(N,C,X):     
    sup = X[N-1]-X[0]
    inf = 0    
    while inf <= sup:                
        med = (inf + sup)//2        
        if esPosibleAcomodarCVacasADistD(C,X,med): # Debo probar con una distancia mas grande
            inf = med + 1
        else: # Debo probar con una distancia mas chica 
            sup = med - 1 
    return sup
        
 
 
# Funcion de verificacion. Chequea si es posible acomodar a las C vacas a distancia D entre ellas
def esPosibleAcomodarCVacasADistD(C,X,D):
    X.sort()     
    contador = 1
    ultimoEstablo = X[0]
    for i in range(1,len(X)): 
        if X[i] - ultimoEstablo >= D: 
            contador = contador + 1
            ultimoEstablo = X[i]
    if contador >= C: 
        return True
    return False
 
 
 
# Leo los inputs e imprimo los outputs
t = int(input()) # Numero de tests a correr
for i in range(t):
    linea = input().split()
    N = int(linea[0])
    C = int(linea[1]) 
    X = []
    for j in range(N): 
        X.append(int(input()))
    # Corro el programa e imprimo soluciones 
    print(aggrcow(N, C, X))
    
    
    