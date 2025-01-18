# Idea: Armo un grafo correspondiente a una red que contenga un sumidero s, conectado mediante ejes de valor a[i] 
#       a las distintas aulas 0, 1, ..., n-1 (que seri�an los nodos 1, 2, ..., n). Este valor a[i] representa el 
#       numero original de alumnos que tenía cada aula i. A estas aulas las considerare que estan en la "primer capa 
#       de aulas". Luego armare una segunda capa de aulas, que contendra a las mismas n aulas pero duplicadas (estas 
#       seran representadas por los nodos n + 1, n + 2, ..., 2 n).  
#       Cada aula i de la primer capa se conectara mediante ejes de peso a[i] con las aulas de la segunda capa que 
#       representen las aulas hacia las cuales hay pasadizos. Ademas, cada aula de la primer capa se debe conectar 
#       con su duplicada de la segunda capa (modelando el hecho de que hay alumnos que podrian tener que quedarse 
#       donde estaban originalmente). Luego, de cada aula de la segunda capa de aulas salen ejes hacia el sumidero t, 
#       cada uno de peso b[i], representando el numero de alumnos que queda finalmente en cada aula. 
#       Si el numero de alumnos iniciales (sumatoria de los a[i]) coincide con el numero de alumnos que lograron ser 
#       acomodados en las aulas de la segunda capa, o en otras palabras, si el numero de alumnos totales coincide con 
#       el flujo maximo a traves de esta red, entonces significa que pueden reacomodarse los alumnos de la manera 
#       pedida; si no, no. 
#       Debemos entonces calcular el flujo maximo a traves de esa red descrita mas arriba. Eso lo hare con el 
#       algoritmo de Ford-Fulkerson (FF).
#       Sobre el algoritmo de FF hice una modificacion para que se vayan registrando los movimientos de flujo de un 
#       aula hacia otra. Para ello trabajo con una matriz "flujos" tal que flujos[i][j] indica cuantos alumnos se 
#       movieron desde el aula i hacia el aula j. 


# Crea el grafo correspondiente a la red deseada, implementado como matriz de adyacencias
def armarGrafo(n, m, a, b, pasajes): 
    G = [[0 for i in range(2 * n + 2)] for j in range(2 * n + 2)]
    for i in range(n): # Completo la fila de la matriz correspondiente a la fuente
        G[0][i + 1] = a[i]
    for i in range(m): # Completo las filas correspondientes a la primer capa de aulas
        aulaU = pasajes[i][0]
        aulaV = pasajes[i][1]
        G[aulaU + 1][aulaV + 1 + n] = a[aulaU]
        G[aulaV + 1][aulaU + n + 1] = a[aulaV]
    for i in range(n): # Pongo ejes entre las aulas de la primer capa con sus duplicadas de la segunda capa 
        G[i + 1][n + i + 1] = a[i]
    for i in range(n + 1 , 2 * n + 1): # Completo las filas correspondientes a la segunda capa de aulas
        G[i][-1] = b[i - n - 1]    
    return G      


# Este código está basado en el algoritmo de Ford-Fulkerson extraído y adaptado de Geek for Geeks. 
# Se hicieron algunas modificaciones para ajustarlo a este problema particular, agregando la funcionalidad 
# relacionada con el registro de movimientos de los alumnos en el grafo.
# Código original: https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
class Graph: # Esta clase representa un grafo dirigido usando una matriz de adyacencia

    def __init__(self, graph):
        self.graph = graph  
        self.ROW = len(graph)
        self.flujos = [[0 for j in range(self.ROW)] for i in range(self.ROW)] # Matriz para registrar los movimientos de los alumnos

    # Devuelve verdadero si encuentra un camino desde s a t en el grafo residual
    # Además, rellena parent[] para recuperar ese camino
    def BFS(self, s, t, parent):
        visited = [False] * self.ROW  # Marcamos todos los vértices como no visitados
        cola = []

        cola.append(s) # Encolamos la fuente s
        visited[s] = True # Y la marcamos como visitada 

        while cola:
            u = cola.pop(0) # Desencolamos un vértice u de la cola

            for vecino, val in enumerate(self.graph[u]): # Para cada vecino del nodo u
                if visited[vecino] == False and val > 0: # Si este no fue visitado y tiene capacidad positiva...
                    cola.append(vecino) # Lo encolamos 
                    visited[vecino] = True # Lo marcamos como visitado
                    parent[vecino] = u # Registramos a su padre 
                    if vecino == t: # Si este vecino ya es el sumidero t, entonces ya sabemos que existe un camino de s a t, frenamos el BFS 
                        return True

        return False # Si llegamos hasta acá, significa que nunca se encontró una conexión al sumidero t 

    # Devuelve el flujo máximo de s a t en un grafo dado
    def FordFulkerson(self, source, sink):
        parent = [-1]*(self.ROW)
        flujo_max = 0 # Flujo máximo acumulado hasta el momento 

        # Mientras existan caminos aumentantes (caminos de s a t con capacidad residual positiva)
        while self.BFS(source, sink, parent):

            # Encontremos la capacidad residual mínima de los ejes a lo largo del camino encontrado por BFS. 
            # O también podemos decir, encontremos el máximo flujo a través del camino encontrado por BFS.

            # El bucle recorre el camino desde el sumidero hasta la fuente usando la lista parent, 
            # buscando la capacidad mínima en las aristas del camino.
            flujo_camino = float("Inf") # Capacidad residual mínima en el camino
            s = sink
            while s != source:
                flujo_camino = min(flujo_camino, self.graph[parent[s]][s])
                s = parent[s]

            # Agregamos el flujo del camino al flujo total
            flujo_max += flujo_camino

            # Actualizamos las capacidades residuales de los ejes y de los ejes inversos a lo largo del camino 
            v = sink
            while v != source:
                u = parent[v]
                # Actualizamos las capacidades residuales y los flujos
                self.graph[u][v] -= flujo_camino
                self.graph[v][u] += flujo_camino
                self.flujos[u][v] += flujo_camino
                if u > v: # Si mandamos flujo de la 2nda capa de aulas a la primera, revertimos flujo que habíamos mandado antes (MUY IMPORTANTE ESTO, ACA ME HABIA TRABADO)
                    self.flujos[v][u] -= flujo_camino
                v = parent[v]

        return flujo_max
    

# Función principal
def aulas(n, m, a, b, pasajes): 
    source = 0 
    sink = 2 * n + 1
    G = armarGrafo(n, m, a, b, pasajes) # Armo matriz de adyacencias que representa la red
    G = Graph(G) # Convierto la matriz G a la clase Graph
    
    # Si el total de alumnos no coincide con el número total de cupos, entonces ya sabemos que no podremos cumplir el objetivo
    totalAlumnos = sum(a)
    cupos = sum(b)
    if totalAlumnos != cupos: 
        return("NO")

    # Buscamos el flujo máximo a través de la red 
    flujoMax = G.FordFulkerson(source, sink)
    
    # Armamos la matriz mov[i][j] que representa cuántos alumnos se movieron desde el aula i hacia el aula j. 
    # Para ello nos quedamos con solo una sección de la matriz G.flujos.
    mov = [[0 for i in range(n)] for j in range(n)]
    for i in range(1, n + 1):
        for j in range(n + 1, 2 * n + 1):
            if G.flujos[i][j] > 0:
                mov[i - 1][j - (n + 1)] = G.flujos[i][j]

    # Finalmente decidimos si es posible realizar el reacomodamiento pedido o no
    if totalAlumnos == flujoMax:
        print("YES")
        for fila in mov:
            print(*fila)
    else: 
        print("NO")
        
        
######### Recepcion del input e impresion del output #########


# Recibimos el input 
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
atajos = []
for i in range(m): 
    u, v = map(int, input().split())
    atajos.append((u - 1, v - 1))

# Corremos la función que ya ella misma se encargará de imprimir 
aulas(n, m, a, b, atajos)
      
        
######### Tests #########

"""
# Test 1   
n = 4
m = 4
a = [1,2,6,3]
b = [3,5,3,1]
pasajes = [(0,1),(1,2),(2,3),(3,1)]
pasajes = [(x - 1, y - 1) for x, y in pasajes]
print(aulas(n, m, a, b, pasajes))

# Test 2 
n = 2
m = 0 
a = [1,2]
b = [2,1]
pasajes = []
pasajes = [(x - 1, y - 1) for x, y in pasajes]
print(aulas(n, m, a, b, pasajes))

# Test 3
n = 10
m = 20
a = [22, 3, 4, 48, 12, 12, 14, 37, 15, 37]
b = [57, 29, 35, 88, 6, 54, 100, 32, 91, 59]
pasajes = [(10, 1), (4, 3), (4, 7), (2, 4), (7, 6), (1, 3), (2, 5), (5, 10), 
          (1, 6), (4, 9), (6, 10), (8, 5), (3, 6), (6, 5), (8, 9), (3, 10), 
          (2, 6), (9, 10), (8, 4), (8, 10)]
pasajes = [(x - 1, y - 1) for x, y in pasajes]
print(aulas(n, m, a, b, pasajes))

# Test 4
n = 10
m = 20
a = [39, 65, 24, 71, 86, 59, 80, 35, 53, 13]
b = [32, 41, 32, 97, 83, 67, 57, 26, 39, 51]
pasajes = [(8, 10), (5, 9), (5, 7), (10, 2), (4, 7), (10, 7), (5, 4), (2, 3),
           (6, 8), (5, 10), (3, 8), (4, 2), (1, 6), (5, 6), (4, 9), (10, 4), (4, 6), (5, 1), (3, 4), (1,10)]
pasajes = [(x - 1, y - 1) for x, y in pasajes]
print(aulas(n, m, a, b, pasajes))
"""





        
        
        
        
