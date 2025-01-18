import heapq
 
 
def armarGrafo(atajos): 
    n = len(atajos)
    grafo = []
    for i in range(n-1): 
        grafo.append([i+1]) # Coloco aristas desde cada aula hacia la inmediata posterior
    grafo.append([])
    for i in range(1,n): 
        grafo[i].append(i-1) # Coloco aristas desde cada aula hacia la inmediata anterior
    for i in range(n): # Incorporo los atajos
        if atajos[i] != i+1 and atajos[i] != i: 
            grafo[i].append(atajos[i])    
    return grafo 
 
 
def dijkstra(atajos,n): 
    # Inicializaciones
    grafo = armarGrafo(atajos)
    res = [float("inf")] * n 
    res[0] = 0 
    pred = [float("inf")] * n # Aca guardare al padre de cada nodo
    pred[0] = -1 # El primer nodo no tiene padre
    cola = []  # Cola de prioridad (distancia,nodo)
    
    # Proceso vecinos del primer nodo
    for u in grafo[0]: 
        res[u] = 1
        pred[u] = 0
        heapq.heappush(cola, (res[u],u))
        
    # Extraigo nodos de cola de prioridad y proceso a sus vecinos
    while cola: 
        dist, w = heapq.heappop(cola)
        for u in grafo[w]: 
            if res[u] > res[w] + 1: 
                res[u] = res[w] + 1 
                pred[u] = w 
                # Actualizo clave de nodo u en la cola a res[u]
                heapq.heappush(cola, (res[u], u))
    
    return res
 
          
######################### Tests ######################### 
 
 
#atajos = [3,3,3,3,6,6,6]
#print(dijkstra(atajos))
 
#atajos = [1,1,2]
#print(dijkstra(atajos))
 
#atajos = [0,1,2,3,4]
#print(dijkstra(atajos))
 
 
####### Recepción de inputs e impresión de outputs ######
 
 
# Recibo inputs
n = int(input())  
atajos = list(map(int, input().split())) 
# Hago que los nodos se cuenten a partir de 0 
for i in range(n): 
    atajos[i] = atajos[i] - 1 
# Calculo el resultado
res = dijkstra(atajos,n)
# Lo imprimo en el formato solicitado
print(' '.join(map(str, res)))


