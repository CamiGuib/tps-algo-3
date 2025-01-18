# Desarrollo

## Descripción del problema 

En este problema se trata de analizar cómo cambia la conectividad de un ciudad a medida que se eliminan esquinas de un grafo que representa la red de calles. El grafo es un digrafo donde los nodos representan las esquinas de la ciudad y las aristas representan las calles entre ellas.
El problema presenta lo siguiente: 
- se conoce un grafo completo con las distancias entre todas las esquinas de la ciudad.
- las esquinas fueron agregadas en un orden cronológico específico y ahora se va a eliminar una por una en el orden inverso.
- cada vez que se elimina una esquina, se debe calcular la suma de todas las distancias entre los nodos restantes en el grafo.
El objetivo es imprimir la suma de distancias para cada paso de eliminación, considerando los nodos que permanecen activos después de eliminar las esquinas de acuerdo al orden dado.

## Enfoque de la solución 

- Me basé en la idea del **algoritmo de Floyd-Warshall**. Fui agregando las esquinas en el mismo orden en el que fueron agregadas históricamente, y cada vez que agregué una esquina me fijé si cada una de las distancias nodo-nodo mejoraban o no al considerar que paso por esa esquina nueva.
- De esa forma para cada esquina `k` agregada fui actualizando una matriz `M[i][j]` con las mejores distancias nodo `i` - nodo `j` encontradas hasta el momento. 
- Y para cada una de esas matrices M calculé la suma de todos sus valores.
