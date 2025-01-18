#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
#include <climits>
#include <queue>

using namespace std;

/*
Idea: 
- corro dijkstra desde nodo 0 hacia todos los nodos y guardo esas dist en vector distDesdePrim. Ademas guardo distancia desde el nodo 0 a n-1 en variable D
- corro dijkstra desde nodo n-1 hasta todos los nodos y guardo dist en vector distDesdeUlt
- Reviso una por una las aristas (u,v) y chequeo: w(u,v)+distDesdePrim[u]+distDesdeUlt[v] == D or w(u,v)+distDesdePrim[v]+distDesdeUlt[u] == D
Si el chequeo da ok lo agrego a lista cm
- Tomo todas las aristas de cm y voy sumando sus longitudes. A esa suma le llamo L. 
- La respuesta es 2 * L 
*/

vector<vector<pair<int, long long>>> armarGrafo(int n, int m, vector<tuple<int, int, long long>>& E) {
vector<vector<pair<int, long long>>> G(n);
for (int i = 0; i < m; i++) {
    int u, v;
    long long w;
    tie(u, v, w) = E[i];
    if (u != v) {
        G[u].emplace_back(v, w);
        G[v].emplace_back(u, w);
    } else {
        G[u].emplace_back(v, w);
    }
}
return G;
}

vector<long long> dijkstra(int n, const vector<vector<pair<int, long long>>>& G, int nodo_inicial) {
vector<long long> dist(n, LLONG_MAX);
vector<int> pred(n, -1);
vector<bool> visit(n, false);
dist[nodo_inicial] = 0;
for (int i = 0; i < n; i++) {
    int v = -1;
    for (int j = 0; j < n; j++) {
        if (!visit[j] && (v == -1 || dist[j] < dist[v])) {
            v = j;
        }
    }
    if (dist[v] == LLONG_MAX) break;
    visit[v] = true;
    for (auto& e : G[v]) {
        int hacia = e.first;
        long long longitud = e.second;
        if (dist[v] + longitud < dist[hacia]) {
            dist[hacia] = dist[v] + longitud;
            pred[hacia] = v;
        }
    }
}
return dist;
}

long long seguridad(int n, int m, vector<tuple<int, int, long long>>& E) {
auto G = armarGrafo(n, m, E);
auto distDesdePrim = dijkstra(n, G, 0);
auto distDesdeUlt = dijkstra(n, G, n - 1);
long long D = distDesdePrim[n - 1];
vector<tuple<int, int, long long>> cm;
for (auto& e : E) {
    int u, v;
    long long w;
    tie(u, v, w) = e;
    if (w + distDesdePrim[u] + distDesdeUlt[v] == D or w + distDesdePrim[v] + distDesdeUlt[u] == D) {
        cm.push_back(e);
    }
}
long long L = 0;
for (auto& e : cm) {
    L += get<2>(e);
}
return 2 * L;
}

int main() {

int n, m;
cin >> n >> m;
vector<tuple<int, int, long long>> E;
for (int i = 0; i < m; i++) {
    int u, v;
    long long w;
    cin >> u >> v >> w;
    E.emplace_back(u, v, w);
}
cout << seguridad(n, m, E) << endl;

return 0;
}
     
     



     


