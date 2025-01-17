# Black or white - BORW 

## Descripción del problema

Se tiene una secuencia de números y se debe asignar un color a cada número: negro, blanco o sin pintar. Las restricciones son: <br>
- Los números pintados de negro deben quedar en orden ascendente estrictamente
- Los números pintados de blanco deben quedar en orden descendente estrictamente
El objetivo es tratar de minimizar el número de números que quedan sin pintar, respetando estas restricciones.

## Enfoque de la solución

Resuelvo este problema utilizando **programación dinámica bottom-up**. Como estructura de memoización utilizo una matriz de 3 dimenciones, `dp[i][ultB][ultN]` donde 
- `i` es el índice del número que se está mirando
- `ultB` es el índice del último número pintado de negro
- `ultN` es el índice del último número pintado de blanco
El valor almacenado en `dp[i][ultB][ultN]` representa el número mínimo de elmeentos qe quedarían sin pintar si estamos en el estado `i` y los últimos números pinrados de blanco y negro son `ultB y `ultN` respectivamente.


