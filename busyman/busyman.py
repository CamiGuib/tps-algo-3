# Idea: 
# Resuelvo el problema con algoritmo greedy.
# Ordeno a las actividades segun su tiempo de finalización. 
# Tomo como primera actividad a la primera actividad de la lista ordenada.
# Tomo como segunda actividad a la primera actividad de la lista ordenada tal que su tiempo de inicialización sea posterior al tiempo de finalización de la anterior.
# Así sucesivamente.
# Retorno el numero de actividades que tome a lo largo de este proceso.



# Funcion principal
def i_am_very_busy(N,X): 
    X_ordenado = sorted(X, key = lambda x: x[1])
    contador = 1
    ultimaAct = X_ordenado[0]
    for i in range(1,len(X)):
        if X_ordenado[i][0] >= ultimaAct[1]: 
            ultimaAct = X_ordenado[i]
            contador = contador + 1 
    return contador
 
 

# Recibo los inputs e imprimo los outputs 
t = int(input()) # Numero de tests 
for test in range(t): 
    N = int(input()) 
    X = [] 
    for i in range(N): 
        linea = input().split() 
        primerCoord = int(linea[0])
        segCoord = int(linea[1])
        X.append((primerCoord,segCoord))
    print(i_am_very_busy(N, X))
 

