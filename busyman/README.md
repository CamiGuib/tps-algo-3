# Busyman 

## Descripción del problema

El objetivo es determinar la cantidad máxima de actividades que una persona puede realizar, dado que cada actividad tiene un tiempo de inicio y un tiempo de finalización. Una persona solo puede realizar una actividad a la vez, y una actividad debe comenzar después de que la anterior haya terminado.

## Enfoque de la solución

Resuelvo este problema con un algoritmo **greedy**. <br>
Ordeno las actividades según su tiempo de finalización en orden ascendente. Tomo como primera actividad a la de menor tiempo de finalización. Luego tomo como segunda actividad a la primera en la lista tal que su tiempo de inicialización sea posterior al tiempo de finalizción de la anterior. Así sucesivamente. 
