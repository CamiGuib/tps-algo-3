# Black or White - BORW

## Descripción del problema

Se tiene una secuencia de números y se debe asignar un color a cada número: negro, blanco o sin pintar. Las restricciones son:
- Los números pintados de negro deben quedar en orden ascendente estrictamente.
- Los números pintados de blanco deben quedar en orden descendente estrictamente.

El objetivo es tratar de minimizar el número de números que quedan sin pintar, respetando estas restricciones.

## Enfoque de la solución

### Representación del estado
Resuelvo este problema utilizando **programación dinámica bottom-up**. Como estructura de memoización utilizo una matriz de 3 dimensiones, ``dp[i][ultB][ultN]``, donde:
- ``i`` es el índice del número que se está mirando.
- ``ultB`` es el índice del último número pintado de negro.
- ``ultN`` es el índice del último número pintado de blanco.

El valor almacenado en ``dp[i][ultB][ultN]`` representa el número mínimo de elementos que quedarían sin pintar si estamos en el estado ``i`` y los últimos números pintados de blanco y negro son ``ultB`` y ``ultN``, respectivamente.

### Transición entre estados
Para cada número de la secuencia, se consideran 4 posibilidades:
1. Si es válido pintar de blanco y negro.
2. Si solo es válido pintar de blanco.
3. Si solo es válido pintar de negro.
4. Si no es viable pintar ni de blanco ni de negro.

En cada caso, se actualiza el valor de ``dp[i][ultB][ultN]`` tomando el mínimo entre las opciones disponibles.

### Caso base
El caso base es cuando ``i = N``.

### Resultado final
Devuelvo el valor mínimo de ``dp[0]``.
