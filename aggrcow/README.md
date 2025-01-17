# Aggressive Cows

## Descripción del problema
Se tiene un número de establos alineados en una línea, cada uno con una posición distinta. Queremos ubicar a un número dado de vacas en estos establos, de tal manera que la distancia mínima entre dos vacas cualquiera sea lo mayor posible.

## Enfoque de la solución
Hago una búsqueda binaria con el objetivo de encontrar la distancia óptima. A la búsqueda binaria la comienzo usando como límite inferior el valor 0 (pues una distancia menor a eso es imposible) y como límite superior (sup) la distancia entre el último y el primer establo (pues una distancia mayor a esa es imposible). En cada paso, chequeo con una función de verificación si es posible acomodar a las `C` vacas a esa distancia dada: si es posible, pruebo con una distancia mayor; si no es posible, pruebo con una distancia menor.  
La función de verificación determina si es posible colocar todas las vacas con una distancia mínima `d` entre ellas. Coloca la primera vaca en el primer establo. Luego acomoda la siguiente a una distancia de al menos `d`. Así sucesivamente. Y luego se fija si se pudieron acomodar de esta manera todas las vacas. Es un algoritmo **greedy**.
