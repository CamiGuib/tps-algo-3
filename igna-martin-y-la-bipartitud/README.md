# Igna, Martín y la bipartitud

## Descripción del problema 

El problema consiste en un árbol (grafo conexo y sin ciclos) dado con n nodos y n-1 aristas. El objetivo es determinar el número máximo de aristas que se pueden agregr al árbol dado, cumpliendo las siguientes condiciones: <br> 
1- El grafo debe seguir siendo bipartito (los nodos se pueden dividir en dos conjuntos A y B de forma tal que todas las aristas conectan un nodo de A con un nodo de B (y nunca dos nodos del mismo conjunto)). <br>
2- El grafo debe ser simple (no se permiten loops ni aristas múltiples). <br>

## Enfoque de la resolución

- El árbol se representa como una lista de adyacencias `G` con `n` nodos.
- Se realiza **BFS (Breadth First Search)** desde un nodo raíz para dividir los nodos del grafo en dos conjuntos: `part_par` (nodos a distancia par del nodo raíz) y `part_impar` (nodos a distancia impar del nodo raíz). 
- Calculo cuántas aristas tendría un grafo completo de |part_par| nodos en la partición part_par y |part_impar| en la partición part_impar y a eso le resto el número de aristas del grafo original. Eso sería la respuesta. 
