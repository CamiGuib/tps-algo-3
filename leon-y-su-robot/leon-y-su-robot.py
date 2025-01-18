#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>

using namespace std;


/*
Idea: 
- Armo un grafo G (implementado como una lista de adyacencias) donde cada nodo representa una pieza y cada arista (u,v) representa la mejor oferta especial que hubiera entre la pieza u y la pieza v.
- Corro el algoritmo de Prim con cola de prioridad sobre el grafo para obtener el AGM. Durante la ejecucion del algoritmo se tienen en cuenta tanto las mejores ofertas especiales (las presentes en el grafo) como los costos tradicionales dados por a[i] + a[j].
- Retorno la suma total de todos los costos de todas las aristas del AGM, que seria la respuesta del problema.
*/ 


// Funcion que arma el grafo solo con las mejores ofertas
// Es decir, si entre dos nodos hay varias ofertas disponibles, se queda solo con la mejor 
// G no es multigrafo
vector<vector<pair<int, long long>>> armarGrafo(int n, int m, vector<tuple<int, int, long long>> &ofertas) {
vector<vector<pair<int, long long>>> G(n); // Lista de adyacencias [[(nodo, peso)]]
map<pair<int, int>, long long> mejores_ofertas; // Diccionario para almacenar las mejores ofertas 

// Procesamos cada oferta
for (auto &oferta : ofertas) {
    int u = get<0>(oferta);
    int v = get<1>(oferta);
    long long w = get<2>(oferta);

    if (u > v) {
        swap(u, v); // Para asegurarnos de que cada (u, v) este ordenado
    }

    // Guardamos la mejor oferta
    if (mejores_ofertas.find({u, v}) == mejores_ofertas.end() || mejores_ofertas[{u, v}] > w) {
        mejores_ofertas[{u, v}] = w;
    }
}

// Construimos el grafo a partir de las mejores ofertas
for (auto &[key, peso] : mejores_ofertas) {
    int u = key.first;
    int v = key.second;
    G[u].emplace_back(v, peso);
    G[v].emplace_back(u, peso);
}

return G;
}


long long prim_trivial(int n, int m, vector<long long> &a, vector<tuple<int, int, long long>> &ofertas) {
// Creamos el grafo con las mejores ofertas
vector<vector<pair<int, long long>>> G = armarGrafo(n, m, ofertas);
long long res = 0;
vector<bool> visitados(n, false);
priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> heap;

// Elegimos el nodo inicial como el de menor costo en a
int nodo_inicial = min_element(a.begin(), a.end()) - a.begin();
visitados[nodo_inicial] = true;

// Agregamos las ofertas del nodo inicial al heap
for (auto &[vecino, peso] : G[nodo_inicial]) {
    heap.emplace(peso, vecino);
}

// Agregamos conexiones directas al nodo inicial mediante a
for (int i = 0; i < n; i++) {
    if (i != nodo_inicial) {
        heap.emplace(a[i] + a[nodo_inicial], i);
    }
}

// Procesamos los nodos restantes
while (!heap.empty()) {
    auto [peso, u] = heap.top();
    heap.pop();

    if (!visitados[u]) {
        visitados[u] = true;
        res += peso;

        // Agregamos al heap los vecinos no visitados
        for (auto &[vecino, peso_arista] : G[u]) {
            if (!visitados[vecino]) {
                heap.emplace(peso_arista, vecino);
            }
        }
    }
}

return res;
}


int main() {

/* Tests */
/*
// Test 1
{
    int n = 3, m = 2;
    vector<long long> a = {1, 3, 3};
    vector<tuple<int, int, long long>> ofertas = {{1, 2, 5}, {1, 0, 1}};
    cout << "Resultado Test 1: " << prim_trivial(n, m, a, ofertas) << " (Esperado: 5)" << endl;
}

// Test 2
{
    int n = 4, m = 0;
    vector<long long> a = {1, 3, 3, 7};
    vector<tuple<int, int, long long>> ofertas = {};
    cout << "Resultado Test 2: " << prim_trivial(n, m, a, ofertas) << " (Esperado: 16)" << endl;
}

// Test 3
{
    int n = 5, m = 4;
    vector<long long> a = {1, 2, 3, 4, 5};
    vector<tuple<int, int, long long>> ofertas = {{0, 1, 8}, {0, 2, 10}, {0, 3, 7}, {0, 4, 15}};
    cout << "Resultado Test 3: " << prim_trivial(n, m, a, ofertas) << " (Esperado: 18)" << endl;
}*/


// Leemos el input
int n, m;
cin >> n >> m;
vector<long long> a(n);
for (int i = 0; i < n; i++) {
    cin >> a[i];
}
vector<tuple<int, int, long long>> ofertas(m);
for (int i = 0; i < m; i++) {
    int u, v;
    long long w;
    cin >> u >> v >> w;
    ofertas[i] = {u - 1, v - 1, w};
}

// Corremos el programa e imprimimos el output
cout << prim_trivial(n, m, a, ofertas) << '\n';


return 0;


}
