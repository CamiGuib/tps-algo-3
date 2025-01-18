# Juli y los túneles de Exactas

# Descripción del problema

Juli quiere calcular la mínima energía necesaria para llegar desde el aula 1 a cualquier otra aula `i` en la Facultad de Ciencias Exactas. Para moverse entre aulas tiene dos opciones: 
- Caminar normalmente: esto requiere una cantidad de energía igual a `|i-j|`, donde `j` es el aula de origen y `i` es el aula de destino.
- Usar un atajo: cada aula i tiene un atajo unidireccional hacia otra aula a<sub>i</sub>, que cuesta exactamente 1 unidad de energía. Los atajos tienen la propiedad de que i ≤ a<sub>i</sub> ≤ n y son crecientes a<sub>i</sub> ≤ a<sub>i+1</sub>.

