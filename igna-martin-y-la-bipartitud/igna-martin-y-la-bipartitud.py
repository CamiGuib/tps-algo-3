#include <iostream>
#include <vector>
#include <queue>

using namespace std;


/*
Idea: 
- El arbol se representa como una lista de adyacencias G con n nodos.
- Se realiza BFS desde un nodo raiz para dividir los nodos del grafo en dos conjuntos: part_par (nodos a distancia par del nodo raiz) y part_impar (nodos a distancia impar del nodo raiz).
- Calculo cuantas aristas tendria un grafo completo de |part_par| nodos en la particion part_par y |part_impar| en la particion part_impar y a eso le resto el numero de aristas del grafo original. Eso seria la respuesta.
*/ 


long long cuantas_aristas_para_ser_bip_completo(vector<vector<int>>& G, int n) {
queue<int> q; // Inicializo cola vacia
vector<int> dist(n, -1); // Inicializo vector de distancias a la raiz

long long part_par = 0;   // Contador de nodos en nivel par
long long part_impar = 0; // Contador de nodos en nivel impar

// Relleno con datos del primer nodo
q.push(0); // Pongo en la cola al primer nodo
dist[0] = 0; // Registro la distancia del primer nodo
part_par += 1; // Ya recorri un nodo de nivel 0, sumo 1 a part_par

while (!q.empty()) { // Mientras la cola no este vacia
    int nodo = q.front();
    q.pop();
    for (int vecino : G[nodo]) {
        if (dist[vecino] == -1) { // Si vecino no fue visitado
            dist[vecino] = dist[nodo] + 1;
            q.push(vecino);
            if (dist[vecino] % 2 == 0) {
                part_par += 1;
            } else {
                part_impar += 1;
            }
        }
    }
}

return part_impar * part_par - (n-1); // Todas las aristas que tendria un grafo completo menos las que ya estaban en el grafo G
}



int main() {
// Leemos los inputs e imprimimos los outputs
int n;
while (cin >> n) { // Leemos el número de nodos
    if (n == 0) break; // Si n es 0, terminamos el programa

    vector<vector<int>> G(n); // Grafo G implementado como lista de adyacencias
    
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        u--; v--; // Hacemos que los nodos comiencen a contar desde 0
        G[u].push_back(v);
        G[v].push_back(u);
    }

    cout << cuantas_aristas_para_ser_bip_completo(G, n) << endl; // Calculo e imprimo el resultado
}

return 0;
}



