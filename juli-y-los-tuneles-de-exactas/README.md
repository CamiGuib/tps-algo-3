# Juli y los túneles de Exactas

# Descripción del problema

Juli quiere calcular la mínima energía necesaria para llegar desde el aula 1 a cualquier otra aula `i` en la Facultad de Ciencias Exactas. Para moverse entre aulas tiene dos opciones:

1. Caminar normalmente: esto requiere una cantidad de energía igual a `|i-j|`, donde `j` es el aula de origen y `i` es el aula de destino.
2. Usar un atajo: cada aula `i` tiene un atajo unidireccional hacia otra aula `ai`, que cuesta exactamente `1` unidad de energía. Los atajos tienen la propiedad de que `i ≤ ai ≤ n` y son crecientes `ai ≤ ai+1`.

El objetivo es calcular un arreglo `m`, donde cada `m[i]` representa la energía mínima necesaria para ir desde el aula 1 hasta el aula `i`.


# Enfoque de la solución

Modelo a este problema con un grafo y utilizo el **algoritmo de Dijkstra** implementado con cola de prioridad, para encontrar el costo mínimo de energía necesaria para llegar desde el aula 1 hasta cada una de las aulas.  
Detallo acá:  
- Construyo grafo donde cada nodo (aula) tiene una arista hacia su aula inmediata posterior e inmediata anterior con costo 1. Los atajos se modelan como aristas adicionales de costo fijo igual a 1, según el arreglo de atajos dado.  
- Aplico Dijkstra para calcular la distancia mínima desde el nodo 0 (aula inicial) hasta cada nodo. La estructura cola de prioridad asegura que se procesen primero los nodos con menor distancia acumulada.  

