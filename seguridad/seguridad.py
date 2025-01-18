# Idea: 
# - corro dijkstra desde nodo 0 hacia todos los nodos y guardo esas dist en vector distDesdePrim. Ademas guardo distancia desde el nodo 0 a n-1 en variable D
# - corro dijkstra desde nodo n-1 hasta todos los nodos y guardo dist en vector distDesdeUlt
# - Reviso una por una las aristas (u,v) y chequeo: w(u,v)+distDesdePrim[u]+distDesdeUlt[v] == D or w(u,v)+distDesdePrim[v]+distDesdeUlt[u] == D. Si el chequeo da ok lo agrego a lista cm
# - Tomo todas las aristas de cm y voy sumando sus longitudes. A esa suma le llamo L. 
# - La respuesta es 2 * L 



# Implementa al grafo como lista de adyacencias
def armarGrafo(n, m, E): 

    G = [[] for k in range(n)] # Lista de adyacencias [[(nodo, longitud)]]
    for i in range(m): 
        if E[i][0] != E[i][1]: # Si la arista no es bucle 
            G[E[i][0]].append((E[i][1] , E[i][2]))
            G[E[i][1]].append((E[i][0] , E[i][2]))
        else: # Si la arista es bucle 
            G[E[i][0]].append((E[i][1] , E[i][2]))
    return G 



# Codigo inspirado en Dijkstra de cp-algorithms 
def dijkstra(n, G, nodo_inicial): 
    dist = [float("inf") for k in range(n)]
    pred = [-1 for k in range(n)]
    visit = [False for k in range(n)]
    
    dist[nodo_inicial] = 0
    
    for i in range(n):
        v = -1 
        for j in range(n): 
            if not visit[j] and (v == -1 or dist[j] < dist[v]): 
                v = j
                
        if dist[v] == float("inf"): 
            break 
        
        visit[v] = True
        
        for e in G[v]: 
            hacia = e[0]
            long = e[1]
            
            if dist[v] + long < dist[hacia]:
                dist[hacia] = dist[v] + long 
                pred[hacia] = v 
    
    return dist
                


def seguridad(n, m, E): 
    G = armarGrafo(n, m, E)
    distDesdePrim = dijkstra(n, G, 0)
    distDesdeUlt = dijkstra(n, G, n - 1)
    D = distDesdePrim[n - 1]
    cm = []
    for e in E: 
        if e[2] + distDesdePrim[e[0]] + distDesdeUlt[e[1]] == D or e[2] + distDesdePrim[e[1]] + distDesdeUlt[e[0]] == D: # Si la arista pertenece a camino minimo de 0 a n-1 
            cm.append(e)
    L = 0 
    for i in range(len(cm)): 
        L += cm[i][2]
    
    return 2 * L
    
        
          
# Leo el input
n, m = map(int, input().split())   
E = []
for i in range(m):
    u, v, w = map(int, input().split())  
    E.append((u, v, w))
 
# Imprimo el output
print(seguridad(n,m,E))
 

