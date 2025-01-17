# Aggresive cows 

## Descripción del problema 
Se tiene un número de establos alineados en una línea, cada uno con una posición distinta. Queremos ubicar a un número dado de vacas en estos establos, de tal manera que la distancia mínima entre dos vacas cualquiera sea lo mayor posible.

## Enfoque de la solucion
Hago una busqueda binaria con el objetivo de encontrar la distancia optima. A la busqueda binaria la comienzo usando como limite inferior el valor 0 (pues distancia menor a eso es imposible) y como limite superior (sup) a la distancia entre el ultimo y el primer establo (pues distancia mayor a esa es imposible). En cada paso chequeo con una funcion de verificacion si es posible acomodar a las C vacas a esa dada distancia: si es posible, pruebo con una distancia mayor; si no es posible, pruebo con una distancia menor. <br>
La función de verificación determina si es posible colocar todas las vacas con una distancia mínima d entre ellas. Coloca la primera vaca en el primer establo. Luego acomoda la siguiente a distancia al menos d. Así sucesivamente. Y luego se fija si se pudieron acomodar de esta manera todas las vacas. Es un algoritmo greedy. 
