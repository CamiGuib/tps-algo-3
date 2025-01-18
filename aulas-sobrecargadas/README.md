# Aulas sobrecargadas

## Descripción del problema 

Este problema plantea una situación en la que hay n aulas con una cantidad `ai` de estudiantes en cada una, pero las aulas tienen una capacidad máxima de `bi` estudiantes. La tarea es determinar si es posible reorganizar a los estudiantes entre las aulas para que cada una contenga exactamente `bi` estudiantes, teniendo en cuenta que algunos pares de aulas están conectados, lo que permite mover estudiantes entre ellas, de acuerdo a las siguientes reglas: 
- un alumno puede moverse de un aula a otra si existe una conexión entre ambas (es bidireccional).
- un alumno no puede realizar múltiples movimientos, solo uno.

## Enfoque de la solución

-Armo un grafo correspondiente a una red que contenga un sumidero s, conectado mediante ejes de valor a[i] 
a las distintas aulas 0, 1, ..., n-1 (que serían los nodos 1, 2, ..., n). Este valor a[i] representa el 
número original de alumnos que tenía cada aula i. A estas aulas las consideraré que están en la "primer capa 
de aulas". Luego armaré una segunda capa de aulas, que contendrá a las mismas n aulas pero duplicadas (estas 
serán representadas por los nodos n + 1, n + 2, ..., 2 n).  

Cada aula i de la primer capa se conectará mediante ejes de peso a[i] con las aulas de la segunda capa que 
representen las aulas hacia las cuales hay pasadizos. Además, cada aula de la primer capa se debe conectar 
con su duplicada de la segunda capa (modelando el hecho de que hay alumnos que podrían tener que quedarse 
donde estaban originalmente). Luego, de cada aula de la segunda capa de aulas salen ejes hacia el sumidero t, 
cada uno de peso b[i], representando el número de alumnos que queda finalmente en cada aula. 

Si el número de alumnos iniciales (sumatoria de los a[i]) coincide con el número de alumnos que lograron ser 
acomodados en las aulas de la segunda capa, o en otras palabras, si el número de alumnos totales coincide con 
el flujo máximo a través de esta red, entonces significa que sí pueden reacomodarse los alumnos de la manera 
pedida; si no, no. 

Debemos entonces calcular el flujo máximo a través de esa red descrita más arriba. Eso lo haré con el 
algoritmo de Ford-Fulkerson (FF). 

Sobre el algoritmo de FF hice una modificación para que se vayan registrando los movimientos de flujo de un 
aula hacia otra. Para ello trabajo con una matriz "flujos" tal que flujos[i][j] indica cuántos alumnos se 
movieron desde el aula i hacia el aula j. 
