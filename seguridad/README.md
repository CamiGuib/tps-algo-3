# Seguridad

## Descripción del problema 

El problema plantea un multigrafo no dirigido que representa las calles y esquinas de una ciudad. El objetivo es determinar el costo total de instalar sistemas de seguridad en todas las calles que pertenecen a algún camino mínimo entre las esquinas `0` y `n-1`. Las calles tienen una longitud asociada, y el costo de cubrir una calle es el doble de su longitud. <br> 
Se debe identificar todas las calles que son parte de algún camino mínimo entre `0` y `n-1` y calcular el costo total para cubrirlas. 

## Enfoque de la solución

- Corro el **algoritmo de Dijkstra** desde nodo `0` hacia todos los nodos y guardo esas distancias en un vector `distDesdePrim`. Además guardo distancia desde el nodo `0` a `n-1` en variable `D`.
- Corro Dijkstra desde el nodo `n-1` hasta todos los nodos y guardo esas distancias en vector `distDesdeUlt`.
- Reviso una por una las aristas `(u,v)` y chequeo: `w(u,v) + distDesdePrim[u] + distDesdeUlt[v] == D or w(u,v) + distDesdePrim[v] + distDesdeUlt[u] == D`. Si el chequeo da ok lo agrego a lista `cm`.
- Tomo todas las aristas de `cm` y voy sumando sus longitudes. A esa suma le llamo `L`. 
- La respuesta es `2 * L`. 
