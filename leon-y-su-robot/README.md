# León y su robot 

## Descripción del problema

Este es un clásico problema de conexión mínima de un grafo. León tiene n piezas robóticas que deben ser unidas para formar una estructura conectada, y para unir dos piezas debe pagar un costo determinado. El costo de unir dos piezas depende de sus valores `a[i]` y `a[j]`, con el costo de unirlas `a[i] + a[j]`. Sin embargo hay ofertas especiales que permiten unir ciertas piezas a un costo fijo `w`, que puede ser menor que el costo tradicional. <br>
El objetivo es encontrar el mínimo costo que podría pagar León al unir todaslas piezas, usando o no las ofertas especiales disponibles. 

## Enfoque de la solución 

- Armo un grafo `G` (implementado como una lista de adyacencias) donde cada nodo representa una pieza y cada arista `(u,v)` representa la mejor oferta especial que hubiera entre la pieza `u` y la pieza `v`.
- Corro el **algoritmo de Prim** con cola de prioridad sobre el grafo para obtener el árbol generador mínimo (AGM). Durante la ejecución del algoritmo se tienen en cuenta tanto las mejores ofertas especiales (las presentes en el grafo) como los costos tradicionales dados por `a[i] + a[j]`.
- Retorno la suma total de todos los costos de todas las aristas del AGM, que sería la respuesta del problema.
