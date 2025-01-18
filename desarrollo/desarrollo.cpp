/*
Me base en la idea del algoritmo de Floyd-Warshall. Fui agregando las esquinas en el mismo orden en el que fueron agregadas historicamente, y cada vez que agregue una esquina me fije si cada una de las distancias nodo-nodo mejoraban o no al considerar que paso por esa esquina nueva.
De esa forma para cada esquina k agregada fui actualizando una matriz M[i][j] con las mejores distancias nodo i - nodo j encontradas hasta el momento.
Y para cada una de esas matrices M calcule la suma de todos sus valores.
*/


#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;


// Funcion que suma los valores M[i][j] para i,j pertenecientes a un conjunto fila_col
long long suma_matriz(const vector<vector<long long>>& M, const vector<long long>& fila_col) {
long long res = 0;
for (long long i : fila_col) {
    for (long long j : fila_col) {
        res += M[i][j];
    }
}
return res;
}


vector<long long> desarrollo(long long n, vector<vector<long long>> d, vector<long long> orden) {

vector<long long> res;
reverse(orden.begin(), orden.end()); // Invierto el orden para ir agregando las esquinas en el mismo orden en el que fueron agregadas historicamente
vector<vector<long long>> M = d;
vector<long long> esq_agregadas;

for (long long k : orden) {
    esq_agregadas.push_back(k);
    // Actualizo la matriz M
    for (long long i = 0; i < n; i++) {
        for (long long j = 0; j < n; j++) {
            M[i][j] = min(M[i][j], M[i][k] + M[k][j]);
        }
    }
    // Hago la suma de los valores de la matriz teniendo en cuenta solamente las esquinas que fueron agregadas hasta ahora 
    res.push_back(suma_matriz(M, esq_agregadas));
}

reverse(res.begin(), res.end());
return res;
}


int main() {

// Leo los inputs
long long n;
cin >> n;

vector<vector<long long>> d(n, vector<long long>(n));
for (long long i = 0; i < n; i++) {
    for (long long j = 0; j < n; j++) {
        cin >> d[i][j];
    }
}

vector<long long> orden(n);
for (long long i = 0; i < n; i++) {
    cin >> orden[i];
    orden[i] = orden[i] - 1; 
}

// Corro la funcion desarrollo
vector<long long> res = desarrollo(n, d, orden);

// Imprimo los outputs
for (long long val : res) {
    cout << val << " ";
}
cout << endl;

return 0;

}
