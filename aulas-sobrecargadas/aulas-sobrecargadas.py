/* 
    Idea: Armo un grafo correspondiente a una red que contenga un sumidero s, conectado mediante ejes de valor a[i] 
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
*/

#include <iostream>
#include <vector>
#include <climits>
#include <queue>
#include <numeric> 

using namespace std;

// Funcion que crea el grafo correspondiente a la red deseada, implementado como matriz de adyacencias
vector<vector<long long>> armarGrafo(long long n, long long m, vector<long long>& a, vector<long long>& b, vector<pair<long long, long long>>& pasajes) {
vector<vector<long long>> G(2 * n + 2, vector<long long>(2 * n + 2, 0)); 
for (long long i = 0; i < n; i++) { // Completo la fila correspondiente a los ejes que van de la fuente a la primer capa de aulas
    G[0][i + 1] = a[i];
}
for (long long i = 0; i < m; i++) { // Completo las filas correspondientes a los ejes que van de la primer capa de aulas a la segunda
    long long aulaU = pasajes[i].first;
    long long aulaV = pasajes[i].second;
    G[aulaU + 1][aulaV + 1 + n] = a[aulaU];
    G[aulaV + 1][aulaU + 1 + n] = a[aulaV];
}
for (long long i = 0; i < n; i++) { // Pongo ejes correspondientes a las aulas de la primera capa consigo mismas en la segunda capa
    G[i + 1][n + i + 1] = a[i];
}
for (long long i = n + 1; i < 2 * n + 1; i++) { // Completo las filas correspondientes a los ejes que van de la segunda capa de aulas al sumidero
    G[i][2 * n + 1] = b[i - n - 1];
}
return G;
}

/* Este codigo esta basado en el algoritmo de Ford-Fulkerson extraido y adaptado de Geek for Geeks
Se hicieron algunas modificaciones para ajustarlo a este problema particular agregando la funcionalidad
relacionada con el registro de movimientos de los alumnos en el grafo.
Codigo original: https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/ */
class Graph { // Esta clase representa un grafo dirigido usando una matriz de adyacencia
public:

vector<vector<long long>> graph;
vector<vector<long long>> flujos;
long long ROW;

Graph(vector<vector<long long>>& graph) {
    this->graph = graph;
    ROW = graph.size();
    flujos = vector<vector<long long>>(ROW, vector<long long>(ROW, 0)); // Matriz para registrar los mov de los alumnos
}

// BFS para encontrar si hay un camino aumentante (camino que va de s a t en el grafo residual)
// Ademas rellena parent[] para recuperar ese camino 
bool BFS(long long s, long long t, vector<long long>& parent) {
    vector<bool> visited(ROW, false);
    queue<long long> cola;
    cola.push(s); // Encolamos la fuente s
    visited[s] = true; // Y la marcamos como visitada

    while (!cola.empty()) {
        long long u = cola.front(); // Desencolamos u vertice u de la cola
        cola.pop();
        for (long long vecino = 0; vecino < ROW; vecino++) { // Para cada vecino de u
            if (graph[u][vecino] > 0 && !visited[vecino]) { // Si este no fue visitado y tiene capacidad positiva
                cola.push(vecino); // Lo encolamos 
                visited[vecino] = true; // Lo marcamos como visitado
                parent[vecino] = u; // Registramos a su padre
                if (vecino == t) { // Si este vecino ya es sumidero, entonces ya sabemos que existe un camino de s a t, frenamos el BFS
                    return true;
                }
            }
        }
    }
    return false; // Si llegamos hasta aca signific que nunca se encontro una conexion al sumidero t
}

// Algoritmo de Ford-Fulkerson
// Devuelve el flujo maximo de s a t en un grafo dado
long long FordFulkerson(long long source, long long sink) {
    vector<long long> parent(ROW, -1);
    long long flujo_max = 0;
    
    while (BFS(source, sink, parent)) { // Mientras existan caminos aumentantes (caminos de s a t con capacidad residual positiva)

        // Encontremos la capacidad residual minima de los ejes a lo largo del camino encontrado por BFS. 
        // O tambien podemos decir, encontremos el maximo flujo a traves del camino encontrado por BFS.

        // El bucle recorre el camino desde el sumidero hasta la fuente usando 
        // la lista parent, buscando la capacidad mínima en las aristas del camino.
        long long flujo_camino = LLONG_MAX; // Capacidad residual minima en el camino
        long long s = sink;
        while (s != source) {
            flujo_camino = min(flujo_camino, graph[parent[s]][s]);
            s = parent[s];
        }

        flujo_max += flujo_camino;
        
        // Actualizamos las capacidades residuales de los ejes y de los ejes inversos a lo largo del camino 
        long long v = sink;
        while (v != source) {
            long long u = parent[v];
            // Actualizamos las capacidades residuales y los flujos
            graph[u][v] -= flujo_camino;
            graph[v][u] += flujo_camino;
            flujos[u][v] += flujo_camino;
            if (u > v){ // Si mando flujo de la 2nda capa de aulas a la primera, revertimos flujo que habiamos mandado antes
                flujos[v][u] -= flujo_camino;
            }
            v = parent[v];
        }
    }
    return flujo_max;
}
};

// Funcion principal
string aulas(long long n, long long m, vector<long long>& a, vector<long long>& b, vector<pair<long long, long long>>& pasajes) {

int totalAlumnos = std::accumulate(a.begin(), a.end(), 0);
int cupos = std::accumulate(b.begin(), b.end(), 0);

if (totalAlumnos != cupos) { // Si el total de alumnos presentes no es igual a la suma de los cupos que debe haber en cada aula, es imposible lograr el objetivo 
    cout << "NO" << endl;
    return "NO";
}

long long source = 0;
long long sink = 2 * n + 1;

vector<vector<long long>> G = armarGrafo(n, m, a, b, pasajes); // Armo matriz de adyacencias que representa la red
Graph graph(G); // Convierto la matriz G a la clase Graph

long long flujoMax = graph.FordFulkerson(source, sink); // Corro Ford-Fulkerson

// Armo la matriz de movimientos (matriz mov[i][j] que indica cuantos alumnos del aula i se movieron al aula j)
vector<vector<long long>> mov(n, vector<long long>(n, 0));
for (long long i = 1; i <= n; i++) {
    for (long long j = n + 1; j <= 2 * n; j++) {
        if (graph.flujos[i][j] > 0) {
            mov[i - 1][j - (n + 1)] = graph.flujos[i][j];
        }
    }
}

// Decidimos ahora si es posible lograr el objetivo
if (totalAlumnos == flujoMax) {
    cout << "YES" << endl;
    // Imprimimos la matriz de movimientos 
    for (const auto& fila : mov) {
        for (long long val : fila) {
            cout << val << " ";
        }
        cout << endl;
    }
    return "YES";
} else {
    cout << "NO" << endl;
    return "NO";
}
}

int main() {

// Recibimos el input 
long long n, m;
cin >> n >> m;

vector<long long> a(n), b(n);
for (long long i = 0; i < n; i++) {
    cin >> a[i];
}
for (long long i = 0; i < n; i++) {
    cin >> b[i];
}

vector<pair<long long, long long>> pasajes(m);
for (long long i = 0; i < m; i++) {
    cin >> pasajes[i].first >> pasajes[i].second;
    // Hacemos que los aulas se numeren a partir de 0 (en vez de 1 como estan en el enunciado)
    pasajes[i].first = pasajes[i].first - 1;
    pasajes[i].second = pasajes[i].second - 1;
}

// Corremos la funcion que ya ella misma se encargara de imprimir 
aulas(n, m, a, b, pasajes);

return 0;
}
